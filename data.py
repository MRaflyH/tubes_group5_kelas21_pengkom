import json
import os


class Data:
    PATH = os.path.join(os.getcwd(), 'data.json')

    def __init__(self):
        with open(self.PATH, "r") as f:
            self.__dict__ = json.loads(f.read())

    def save(self):
        json_data = json.dumps(self, indent=4, default=lambda o: o.__dict__)
        with open(self.PATH, "w") as f:
            f.write(json_data)


data = Data()
