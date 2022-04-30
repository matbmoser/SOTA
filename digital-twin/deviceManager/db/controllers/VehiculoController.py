from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.TipoVehiculoController import TipoVehiculoController

class VehiculoController(BaseController):
    def __init__(self):
        self.tableName = 'Vehiculo'
        super().__init__()
        self.externalTable = TipoVehiculoController()
    
    def deleteByMatricula(self, matricula):
        self.conn.deleteTableElement(table=self.tableName, where="matricula='"+str(matricula)+"'")
    
    def getByMatricula(self, matricula):
        return self.conn.fetchAll(table=self.tableName,where="matricula='"+str(matricula)+"'")   
    
    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="matricula", table=self.tableName)
        return self.values

    def update(self, where="all", matricula=None, tipo=None):
        if where == "all":
            where=None
        setList = []
        
        if(matricula != None): setList.append(("matricula", matricula))

        if(tipo != None): setList.append(("tipo", tipo))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)