import json
from objdict import ObjDict
class Terraform:
    def __init__(self,nuvem,config):
        self.nuvem=nuvem
        self.config=config
        self.data = json.dumps({'global': "val", 'azure': "val"})
    def teste(self):
        print(self.data)
