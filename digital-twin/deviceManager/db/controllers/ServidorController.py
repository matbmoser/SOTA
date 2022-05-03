from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.UniversidadController import UniversidadController

class ServidorController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'Servidor'
        super().__init__()
        self.externalTable = UniversidadController()
    
    def add(self, serverid, socketKey, siglaUni):
        time = str(datetime.now())
        self.tipos = self.externalTable.getValues()
        if(siglaUni not in self.tipos):
            return None
        self.conn.insertTableElement(elem=(serverid, socketKey, self.tipos[siglaUni], time, time), table=self.tableName)
        return True
    
    def deleteByServerId(self, serverid):
        return self.conn.deleteTableElement(table=self.tableName, where="serverid='"+str(serverid)+"'")
    
        
    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getBySocketKey(self, socketKey):
        return self.conn.fetchAll(table=self.tableName,where="socketKey='"+str(socketKey)+"'")
    
    def getByServerId(self, serverid):
        return self.conn.fetchAll(table=self.tableName,where="serverid='"+str(serverid)+"'")      
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="serverid", table=self.tableName)
        return self.values
    
    def getValuesBySocketKey(self):
        self.values = self.conn.getValueIdDict(id="id", value="socketKey", table=self.tableName)
        return self.values
    
    
    def update(self, where="all",  *args, **kwargs):
        if(kwargs["siglaUni"] != None):
            self.tipos = self.externalTable.getValues()
            if(kwargs["siglaUni"] not in self.tipos):
                return None
            idUniversidad = self.tipos[kwargs["siglaUni"]]
            kwargs["idUniversidad"] = idUniversidad
        ignore = ["siglaUni", "self.tipos", "self.externalTable"]
        
        if where == "all":
            where=None
        setList = []
        for var in kwargs:
            if var in ignore:
                continue
            if(kwargs[var] != None): setList.append((var, kwargs[var]))

        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)
        
        return True