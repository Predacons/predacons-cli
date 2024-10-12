from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from predacons import PredaconsEmbedding
import requests
from bs4 import BeautifulSoup
# from googlesearch import search

class VectorStore:
    """
    A class to manage vector storage operations including loading documents,
    splitting text, calculating chunk IDs, and adding documents to a Chroma database.
    """

    def __init__(self, chroma_path, document_path, model=None):
        """
        Initialize the VectorStore with paths and an optional model.

        :param chroma_path: Path to the Chroma database.
        :param document_path: Path to the directory containing documents.
        :param model: Optional model ID for the embedder.
        """
        self.model_id = model if model is not None else None
        self.embedder = PredaconsEmbedding(self.model_id) if self.model_id else PredaconsEmbedding()
        self.chroma_path = chroma_path
        self.document_path = document_path

    def split_text(self, documents: list[Document]):
        """
        Split documents into chunks using RecursiveCharacterTextSplitter.

        :param documents: List of Document objects to be split.
        :return: List of chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        return chunks

    def calculate_chunk_ids(self, chunks):
        """
        Calculate unique IDs for each chunk based on source and page metadata.

        :param chunks: List of chunks to calculate IDs for.
        :return: List of chunks with updated metadata including IDs.
        """
        last_page_id = None
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata.get("source")
            page = chunk.metadata.get("page")
            current_page_id = f"{source}:{page}"

            if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_chunk_index = 0

            chunk_id = f"{current_page_id}:{current_chunk_index}"
            last_page_id = current_page_id
            chunk.metadata["id"] = chunk_id

        return chunks

    def add_to_chroma(self, chunks: list[Document]):
        """
        Add new chunks to the Chroma database if they do not already exist.

        :param chunks: List of chunks to be added to the database.
        """
        db = Chroma(
            persist_directory=self.chroma_path, embedding_function=self.embedder
        )

        chunks_with_ids = self.calculate_chunk_ids(chunks)

        existing_items = db.get(include=[])  # IDs are always included by default
        existing_ids = set(existing_items["ids"])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        new_chunks = []
        for chunk in chunks_with_ids:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)

        if len(new_chunks):
            print(f"👉 Adding new documents: {len(new_chunks)}")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
            db.persist()
        else:
            print("✅ No new documents to add")

    def load_documents(self):
        """
        Load documents from the specified directory.

        :return: List of loaded Document objects.
        """
        loader = DirectoryLoader(self.document_path)
        documents = loader.load()
        return documents

    def load_and_update_db(self):
        """
        Load documents, split them into chunks, and add new chunks to the Chroma database.
        """
        documents = self.load_documents()
        chunks = self.split_text(documents)
        self.add_to_chroma(chunks)

    def load_db(self):
        """
        Load the Chroma database.

        :return: Chroma database object.
        """
        db = Chroma(persist_directory=self.chroma_path, embedding_function=self.embedder)
        return db

    def get_similar(self, query, db=None, top_n=5, similarity_threshold=0.1):
        """
        Retrieve similar documents from the Chroma database based on a query.

        :param query: Query string to search for similar documents.
        :param db: Optional Chroma database object. If None, the database will be loaded.
        :param top_n: Number of top similar documents to retrieve.
        :param similarity_threshold: Minimum similarity score threshold.
        :return: List of tuples containing similar documents and their relevance scores.
        """
        if db is None:
            db = self.load_db()
        results = db.similarity_search_with_relevance_scores(query, k=top_n)
        if len(results) == 0 or results[0][1] < similarity_threshold:
            print(f"Unable to find matching results.")
        
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        return context_text
    
class WebScraper:
    """
    A class to manage web scraping operations including fetching and parsing HTML content.
    """

    def __init__(self):
        pass

    def fetch_html(self, url):
        """
        Fetch HTML content from a given URL.

        :param url: URL to fetch HTML content from.
        :return: HTML content as a string.
        """
        pass

    def parse_html(self, html_content):
        """
        Parse HTML content and extract relevant text.

        :param html_content: HTML content to parse.
        :return: Extracted text as a string.
        """
        pass

    
