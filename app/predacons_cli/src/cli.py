import predacons
import argparse
import os


class Cli:
    def __init__(self):
        self.predacons = predacons

    def launch(self):
        # check if the predacon_cli_config.json file exists
        if not Cli.check_config_file():
            Cli.create_config_file()
        else:
            config = Cli.load_config_file()
    
    def load_model(self, model_path,trust_remote_code=False,use_fast_generation=False, draft_model_name=None,gguf_file=None,auto_quantize=None):
        model = self.predacons.load_model(model_path,trust_remote_code=trust_remote_code,use_fast_generation=use_fast_generation, draft_model_name=draft_model_name,gguf_file=gguf_file,auto_quantize=auto_quantize)
        tokenizer = self.predacons.load_tokenizer(model_path,gguf_file=gguf_file)
        return model, tokenizer
        
    
    def settings(self):
        return self.predacons.settings()
    
    def check_config_file(self):
        file_path = 'predacon_cli_config.json'

        if os.path.exists(file_path):
            return True
        else:
            return False
    
    def create_config_file(self):
        file_path = 'predacon_cli_config.json'
        with open(file_path, 'w') as f:
            f.write('{"model_path": "","trust_remote_code": false,"use_fast_generation": false,"draft_model_name": null,"gguf_file": null,"auto_quantize": null}')
    
    def load_config_file(self):
        file_path = 'predacon_cli_config.json'
        with open(file_path, 'r') as f:
            config = f.read()
        return config
    
        