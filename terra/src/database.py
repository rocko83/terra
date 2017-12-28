#!/usr/bin/env python
from __future__ import print_function
import json
import pymysql

class Database:
    def __init__(self,config):
        self.conn = pymysql.connect(
            host=config.getDados("DB_SERVER"),
            port=3306,
            user=config.getDados("DB_USER"),
            passwd=config.getDados("DB_PASSWD"),
            db=config.getDados("DB_BASE")
        )
        self.cur = self.conn.cursor()

    def queryDatabase(self,string):
        self.cur.execute(string)
        print(self.cur.description)
        print()
        for row in self.cur:
            print(row)

    def closeDatabase(self):
        self.cur.close()
        self.conn.close()

    def printJson(self,id):
        self.cur.execute("select data from projetos2 where id = " + str(id))
        retorno = str(self.cur.fetchone()[0]).strip('^b').replace('\'', '\"')
        retorno = retorno.strip('^\"')
        print(retorno)
        jvar = json.loads(str(retorno))
        print(json.dumps(jvar,indent=4, sort_keys=True))
        #self.cur.execute("insert into projetos2 (name,data) values ")