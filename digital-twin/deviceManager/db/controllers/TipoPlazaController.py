from datetime import datetime
from db.controllers.BaseController import BaseController

class TipoPlazaController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'TipoPlaza'
        super().__init__()


    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getByTipo(self, tipo):
        return self.conn.fetchAll(table=self.tableName,where="tipo='"+str(tipo)+"'")
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="tipo", table=self.tableName)
        return self.values
    