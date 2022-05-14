from datetime import datetime
from db.controllers.BaseController import BaseController
from db.controllers.ZonaController import ZonaController
from db.controllers.VehiculoController import VehiculoController
import hashlib

class PlazaController(BaseController):
    def __init__(self) -> None:
        self.tableName = 'Plaza'
        super().__init__()
        self.externalTable = ZonaController()
        self.externalTable1 = VehiculoController()
    
    def add(self, id, letraZona, matricula):
        time = str(datetime.now())
        self.externalTable.refresh()
        self.tipos = self.externalTable.getValues()
        if(letraZona not in self.tipos):
            return None
        self.externalTable1.refresh()
        self.externalTable1.refresh()
        self.tipos1 = self.externalTable1.getValues()
        if(matricula not in self.tipos1):
            return None
        idZona = self.tipos[letraZona]
        hashDigest = "$token{"+str(time)+str(id)+str(idZona)+"}"
        token = str(hashlib.sha512((hashDigest).encode('utf-8')).hexdigest())
        self.conn.insertTableElementWithId(elem=(id, time, "NULL", 1, 0, idZona, self.tipos1[matricula],token, time, time), table=self.tableName)
        return True
    
    def addTicket(self, id, idZona, idVehiculo):
        time = str(datetime.now())
        hashDigest = "$token{"+str(time)+str(id)+str(idZona)+"}"
        token = str(hashlib.sha512((hashDigest).encode('utf-8')).hexdigest())
        self.refresh()
        return self.conn.insertTableElementWithId(ignore="fechaSalida", elem=(id, time, 1, 0, idZona, idVehiculo,token, time, time), table=self.tableName)
    
    def deleteByMatricula(self, matricula):
        self.tipos1 = self.externalTable1.getValues()
        if(matricula not in self.tipos1):
            return None
        self.conn.deleteTableElement(table=self.tableName, where="idVehiculo='"+str(self.tipos1[matricula])+"'")

    def invalidTicket(self, idVehiculo):
        return self.conn.updateTableElement(table=self.tableName, set=[('valido', 0), ("fechaSalida", str(datetime.now()))], where="idVehiculo='"+str(idVehiculo)+"'")
    
    def deleteByToken(self, token):
        self.conn.deleteTableElement(table=self.tableName, where="token='"+str(token)+"'")
    
    def deleteByIdZona(self, id, idZona):
        self.conn.deleteTableElement(table=self.tableName, where="id="+str(id)+" AND idZona="+str(idZona)+"")

    def get(self, where):
        return self.conn.fetchAll(table=self.tableName, where=where)
    
    def getByValido(self, valido):
        return self.conn.fetchAll(table=self.tableName,where="valido="+str(valido)+"")
    
    def getByIdZona(self, idZona):
        return self.conn.fetchAll(table=self.tableName,where="idZona="+str(idZona)+"")     
    
    def getByIdVehiculo(self, idVehiculo):
        self.refresh()
        self.externalTable1.refresh()
        return self.conn.fetchAll(table=self.tableName,where="idVehiculo="+str(idVehiculo)+"")
    
    def getByIdPlazaZona(self, id, idZona):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+" AND idZona="+str(idZona)+"")
    
    def getByToken(self, token):
        return self.conn.fetchAll(table=self.tableName,where="token="+str(token)+"")        
    
    def getAll(self):
        return self.conn.fetchAll(table=self.tableName)
    
    def getById(self, id):
        return self.conn.fetchAll(table=self.tableName,where="id="+str(id)+"")
    
        
    def getValuesValidoByToken(self):
        self.values = self.conn.getValueIdDict(id="valido", value="token", table=self.tableName)
        return self.values
    
    def getValuesIdVehiculoByToken(self):
        self.values = self.conn.getValueIdDict(id="idVehiculo", value="token", table=self.tableName)
        return self.values
    
    
    def update(self, where="all",  *args, **kwargs):
        if(kwargs["letraZona"] != None):
            self.tipos = self.externalTable.getValues()
            if(kwargs["letraZona"] not in self.tipos):
                return None
            idZona= self.tipos[kwargs["letraZona"]]
            kwargs["idZona"] = idZona
        
        if(kwargs["matricula"] != None):
            self.tipos1 = self.externalTable1.getValues()
            if(kwargs["matricula"] not in self.tipos1):
                return None
            idVehiculo= self.tipos[kwargs["matricula"]]
            kwargs["idVehiculo"] = idVehiculo
        
        ignore = ["letraZona", "matricula"]
        
        if where == "all":
            where=None
            
        setList = []
        for var in kwargs:
            if var in ignore:
                continue
            if(kwargs[var] != None): setList.append((var, kwargs[var]))

        res = self.conn.updateTableElement(table=self.tableName, set=setList, where=where)
        
        return res

