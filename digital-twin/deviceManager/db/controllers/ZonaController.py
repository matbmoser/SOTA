from datetime import datetime
from db.controllers.BaseController import BaseController

class ZonaController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'Zona'
        super().__init__()

    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getByLetra(self, letra):
        return self.conn.fetchAll(table=self.tableName,where="letra='"+str(letra)+"'")
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
    
    def getByIdTipoPlaza(self, idTipoPlaza):
        return self.conn.fetchAll(table=self.tableName,where="idTipoPlaza='"+str(idTipoPlaza)+"'")
           
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="letra", table=self.tableName)
        return self.values
    
    def getValuesIdTipoPlaza(self):
        self.values = self.conn.getValueIdDict(id="id", value="idTipoPlaza", table=self.tableName)
        return self.values
