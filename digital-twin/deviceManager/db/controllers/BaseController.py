import sys
from datetime import datetime
from db.DBManager import DBManager


class BaseController():
    def __init__(self):
        self.conn = DBManager()
        self.fields = self.conn.tables[self.tableName]["keys"]
        self.fieldNames = self.fields["keynames"]
    
    def add(self):
        # Adds new data to table
        return True
    
    def update(self, where="all"):
        ##  Updates with new data
        if where == "all":
            where=None
        setList = []
        pass
    
    def deleteBy(self):
        #Deletes the data
        pass
        
    def getAll(self):
        # Gets all values
        pass
    
    def getValues(self):
        # Gets the values form the main key and id
        pass
    
    def update(self):
        pass