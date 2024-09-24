import predacons

class Cli:
    def __init__(self):
        self.predacons = predacons.Predacons()

    def launch(self):
        self.predacons.launch()