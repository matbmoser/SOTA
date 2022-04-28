from copy import deepcopy
from datetime import datetime
from datetime import datetime
from db.controllers.BaseController import BaseController

class TipoVehiculoController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'TipoVehiculo'
        super().__init__()
        self.values = self.getValues()
    
    def add(self, nombre, ancho, largo, alto):
        time = str(datetime.now())
        if nombre in self.getValues():
            return None
        self.conn.insertTableElement(elem=(nombre, str(ancho),str(largo), str(alto), time, time), table=self.tableName)
        return True
    
    def update(self, where="all", nombre=None, ancho=None, largo=None, alto=None):
        localsList = locals()
        if where == "all":
            where=None
        setList = []
        for var in localsList:
            if(var=="where" or var=="self" or var=="setList"):
                continue
            
            if(localsList[var] != None): setList.append((var, localsList[var]))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)
    
    
    def deleteBySegmento(self, name):
        self.conn.deleteTableElement(table=self.tableName, where="segmento="+str(name))
         
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="segmento", table=self.tableName)
        return self.values
    
    def getValuesByClasificacion(self):
        self.values = self.conn.getValueIdDict(id="id", value="clasificacion", table=self.tableName)
        return self.values
    
if __name__ == "__main__":
    controller = TipoVehiculoController()
    controller.add("SUV",10,56,124)
    controller.update(where="nombre='SUV'", ancho=130, largo=440, alto=1210)