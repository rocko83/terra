import json
class Config:
    def __init__(self,conffile):
        self.conffile = conffile
        self.dados = json.loads(open(self.conffile).read())
    def atualizaJson(self,variavel,valor):
        self.dados[variavel] = valor
        with open(self.conffile, 'w') as confsaida:
            json.dump(self.dados,confsaida)
    def getDados(self,chave):
        return str(self.dados[chave])
    def getData(self,chave):
        return self.dados[chave]