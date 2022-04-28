from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.UniversidadController import UniversidadController

class AparcamientoController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'Aparcamiento'
        super().__init__()
        self.externalTable = UniversidadController()
    
    def add(self, letra, color,  localizacion, siglaUni):
        time = datetime.now().strftime("Y-m-d hh:mm:ss")
        self.tipos = self.externalTable.getTipos()
        if(siglaUni not in self.tipos):
            return None
        self.conn.insertTableElement(elem=(letra, color, localizacion, self.tipos[siglaUni], time, time), table=self.tableName)
        return True
    
    def deleteByLetra(self, letra):
        self.conn.deleteTableElement(table=self.tableName, where="letra="+str(letra))
        
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="letra", table=self.tableName)
        return self.values
    
    def update(self, where="all", letra=None, color=None, localizacion=None, siglaUni=None):
        localsList = locals()
        if where == "all":
            where=None
        setList = []
        for var in localsList:
            if(var=="where" or var=="self" or var=="setList"):
                continue
            
            if(localsList[var] != None): setList.append((var, localsList[var]))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)