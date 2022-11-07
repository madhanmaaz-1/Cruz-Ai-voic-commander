from json import loads
from os import getcwd

class Filehandler:
    def __init__(self):
        pass

    def getRealPath(self, filename):
        return f"""{getcwd()}/{filename}"""

    def getJson(self, filename):
        with open(self.getRealPath(filename), 'r') as jsonFile:
            return loads(jsonFile.read())[0]
    
    def writeFile(self, data, filename):
        with open(self.getRealPath(filename), 'w') as file:
            file.write(data)
            