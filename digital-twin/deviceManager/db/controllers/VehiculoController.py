from datetime import datetime
from datetime import datetime
from BaseController import BaseController
from TipoVehiculoController import TipoVehiculoController

class VehiculoController(BaseController):
    def __init__(self):
        self.tableName = 'Vehiculo'
        super().__init__()
        self.externalTable = TipoVehiculoController()
        
    def add(self, matricula, tipo):
        time = datetime.now().strftime("Y-m-d hh:mm:ss")
        self.tipos = self.externalTable.getValues()
        if(tipo not in self.tipos):
            return None
        self.conn.insertTableElement(elem=(matricula,self.tipos[tipo],time, time), table=self.tableName)
        return True
    
    def deleteByMatricula(self, matricula):
        self.conn.deleteTableElement(table=self.tableName, where="matricula="+str(matricula))
        
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