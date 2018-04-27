#!/usr/bin/env python
from database import Database as Database
from config import Config as Config
from terraform import Terraform as Terraform
from azure import Azclass as Azclass

credenciais = Config("/home/damato/projetos/dados.json")
#base = Database(credenciais)
az = Azclass(credenciais)
models = Config("terraform_models.json")
tf = Terraform("azure",models)
#base.queryDatabase("select data from projetos2 where id = " + str(2))
#base.printJson(2)
#base.closeDatabase()
#conf.atualizaJson("chave","v2")
az.login()


retorno = az.getVmsList("")
if retorno == False:
    print("False")
else:
    print(dir(retorno))
