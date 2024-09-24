import predacons
import argparse


class Cli:
    def __init__(self):
        self.predacons = predacons.Predacons()

    def launch(self):
        self.predacons.launch()
    
    def load_model(self, model_path):
        self.predacons.load_model(model_path)

    def list_models(self):
        self.predacons.list_models()
    
    def clear_model(self):
        self.predacons.clear_model()
    
    def settings(self):
        return self.predacons.settings()