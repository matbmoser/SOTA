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
        
    def add(self, camaraid, socketKey, tipo, protocol, serverid, letra):
        time = str(datetime.now())
        self.tipos1 = self.externalTable1.getValues()
        if(serverid not in self.tipos1):
            return None
        
        self.tipos2 = self.externalTable2.getValues()
        if(letra not in self.tipos2):
            return None
        
        self.conn.insertTableElement(elem=(camaraid, socketKey, tipo, protocol, self.tipos1[serverid], self.tipos2[letra], time, time), table=self.tableName)
        return True
    
    def deleteByCameraId(self,camaraid):
        self.conn.deleteTableElement(table=self.tableName, where="camaraid="+str(camaraid))
    
    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getBySocketKey(self, socketKey):
        return self.conn.fetchAll(table=self.tableName,where="socketKey='"+str(socketKey)+"'")
    
    def getByCameraId(self, cameraid):
        return self.conn.fetchAll(table=self.tableName,where="cameraid='"+str(cameraid)+"'")      
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="camaraid", table=self.tableName)
        return self.values
    
    def getValuesBySocketKey(self):
        self.values = self.conn.getValueIdDict(id="id", value="socketKey", table=self.tableName)
        return self.values
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
                                  
    def update(self, where="all",  camaraid=None, socketKey=None, type=None, protocol=None, serverSocketKey=None, nombreAparcamiento=None):
        localsList = locals()
        if where == "all":
            where=None
        setList = []
        for var in localsList:
            if(var=="where" or var=="self" or var=="setList"):
                continue
            
            if(localsList[var] != None): setList.append((var, localsList[var]))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)