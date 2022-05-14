from datetime import datetime
from db.controllers.BaseController import BaseController

class TipoVehiculoTipoPlazaController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'TipoVehiculoTipoPlaza'
        super().__init__()

    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getByIdTipoPlaza(self, idTipoPlaza):
        return self.conn.fetchAll(table=self.tableName,where="idTipoPlaza='"+str(idTipoPlaza)+"'")
    
    def getByIdTipoVehiculo(self, idTipoVehiculo):
        return self.conn.fetchAll(table=self.tableName,where="idTipoVehiculo='"+str(idTipoVehiculo)+"'")
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
