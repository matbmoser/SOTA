from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.UniversidadController import UniversidadController

class ServidorController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'Servidor'
        super().__init__()
        self.externalTable = UniversidadController()
    
    def add(self, serverid, ip, port, siglaUni):
        time = datetime.now().strftime("Y-m-d hh:mm:ss")
        self.tipos = self.externalTable.getTipos()
        if(siglaUni not in self.tipos):
            return None
        self.conn.insertTableElement(elem=(serverid, ip, port, self.tipos[siglaUni], time, time), table=self.tableName)
        return True
    
    def deleteByMatricula(self, matricula):
        self.conn.deleteTableElement(table=self.tableName, where="matricula="+str(matricula))

    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getBySocketKey(self, socketKey):
        return self.conn.fetchAll(table=self.tableName,where="socketKey='"+str(socketKey)+"'")   
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="serverid", table=self.tableName)
        return self.values
    
    def getValuesBySocketKey(self):
        self.values = self.conn.getValueIdDict(id="id", value="socketKey", table=self.tableName)
        return self.values
    
    
    def update(self, where="all", matricula=None, tipo=None):
        localsList = locals()
        if where == "all":
            where=None
        setList = []
        for var in localsList:
            if(var=="where" or var=="self" or var=="setList"):
                continue
            
            if(localsList[var] != None): setList.append((var, localsList[var]))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)