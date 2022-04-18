from datetime import datetime
from datetime import datetime
from BaseController import BaseController
from TipoVehiculoController import TipoVehiculoController

class UniversidadController(BaseController):
    def __init__(self):
        self.tableName = 'Universidad'
        super().__init__()
        
    def add(self, sigla, nombre, email, telefono, dirección, codigoPostal, ciudad, comunidad, pais):
        time = datetime.now()
        self.conn.insertTableElement(elem=(sigla, nombre, email, telefono, dirección, codigoPostal, ciudad, comunidad, pais,time, time), table=self.tableName)
        return True
    
    def deleteBySigla(self, sigla):
        self.conn.deleteTableElement(table=self.tableName, where="sigla="+str(sigla))
        
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getValues(self):
        self.values = self.conn.getValueIdDict(id="id", value="sigla", table=self.tableName)
        return self.values

    def update(self, where="all", sigla=None, nombre=None, email=None, telefono=None, dirección=None, codigoPostal=None, ciudad=None, comunidad=None, pais=None):
        if where == "all":
            where=None
        setList = []
        
        for var in locals()[1:]:
            fieldName = f'{var=}'.split('=')[0]
            
            if(fieldName != None): setList.append((fieldName, var))
        
        self.conn.updateTableElement(table=self.tableName, set=setList, where=where)