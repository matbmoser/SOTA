from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.ServidorController import ServidorController
from db.controllers.AparcamientoController  import AparcamientoController 

class CamaraController(BaseController):
    def __init__(self):
        self.tableName = 'Camara'
        super().__init__()
        self.externalTable1=ServidorController()
        self.externalTable2=AparcamientoController()
        
    def add(self, cameraid, socketKey, tipo, protocol, serverid, letra):
        time = str(datetime.now())
        self.tipos1 = self.externalTable1.getValues()
        if(serverid not in self.tipos1):
            return None
        
        self.tipos2 = self.externalTable2.getValues()
        if(letra not in self.tipos2):
            return None
        
        self.conn.insertTableElement(elem=(cameraid, socketKey, tipo, protocol, self.tipos1[serverid], self.tipos2[letra], time, time), table=self.tableName)
        return True
    
    def deleteByCameraId(self,cameraid):
        self.conn.deleteTableElement(table=self.tableName, where="cameraid="+str(cameraid))
    
    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getBySocketKey(self, socketKey):
        return self.conn.fetchAll(table=self.tableName,where="socketKey='"+str(socketKey)+"'")
    
    def getByCameraId(self, cameraid):
        return self.conn.fetchAll(table=self.tableName,where="cameraid='"+str(cameraid)+"'")      
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="cameraid", table=self.tableName)
        return self.values
    
    def getValuesBySocketKey(self):
        self.values = self.conn.getValueIdDict(id="id", value="socketKey", table=self.tableName)
        return self.values
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
                                  
    def update(self, where="all", *args, **kwargs):
    
        if(kwargs["serverid"] != None):
            self.tipos = self.externalTable1.getValues()
            if(kwargs["serverid"] not in self.tipos):
                return None
            idServidor= self.tipos[kwargs["serverid"]]
            kwargs["idServidor"] = idServidor
        
        if(kwargs["letra"] != None):
            self.tipos1 = self.externalTable2.getValues()
            if(kwargs["letra"] not in self.tipos1):
                return None
            idAparcamiento= self.tipos1[kwargs["letra"]]
            kwargs["idAparcamiento"] = idAparcamiento
        
        ignore = ["letra", "serverid"]
        
        if where == "all":
            where=None
            
        setList = []
        for var in kwargs:
            if var in ignore:
                continue
            if(kwargs[var] != None): setList.append((var, kwargs[var]))

        res = self.conn.updateTableElement(table=self.tableName, set=setList, where=where)
        
        return res