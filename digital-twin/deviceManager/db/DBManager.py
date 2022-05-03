from datetime import datetime
import sys
sys.path.append("/usr/src/app/")
from operators.op import op
import traceback
import mysql.connector
from db.dbConfig import dbConfig
from datetime import datetime, timezone


class DBManager():
    def __init__(self):
        self.conn = None
        self.tables = None
        self.nTables = 0
        self.operators=[">", "=", "<", "<=", ">=", "!=", "IN"]
        self.version = None
        self.dbname = None
        self.connect()

    def checkIfConnected(self):
        if self.conn.is_connected():
            return True
        return False

    def connect(self):
        try:
            connection = mysql.connector.connect(host=dbConfig.hostname,
                                                 database=dbConfig.dbname,
                                                 user=dbConfig.username,
                                                 password=dbConfig.password)
            if connection.is_connected():
                self.conn = connection
                db_Info = self.conn.get_server_info()
                self.version = db_Info
                cursor = self.conn.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                self.dbname = record[0]
                self.refreshDatabase()
                return True
            else:
                return False
             
        except mysql.connector.Error as e:
            op.printLog(logType="CRITICAL", e=e,messageStr="DBManager.__init__()")
            traceback.print_exc()
            return False
    
    def close(self):
        return self.conn.close()
        
    def refreshDatabase(self):
        self.tables = dict()
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = '" + \
            str(dbConfig.dbname)+"';"
        result = self.query(query)
        for table in result:
            tmpTable = dict()
            tmpTable["name"] = table[0]
            tmpTable["keys"] = self.getTableKeys(tmpTable["name"])
            self.tables[tmpTable["name"]] = tmpTable
        
        #op.printLog(logType="STATS",
         # messageStr="["+str(self.nTables)+"] tables found in ["+str(finiTime-initTime)+"] DBManager.refreshDatabase()")
        return self.tables

    def getTableKeys(self, table):
        keys = dict()
        keynames = list()
        query = "SHOW FIELDS FROM "+str(self.dbname)+"."+str(table)
        result = self.query(query)
        for info in result:
            key = dict()
            key["name"] = info[0]
            keynames.append(key["name"])
            key["type"] = info[1]
            keys[key["name"]] = key
        
        keys["keynames"] = keynames
        return keys

    def query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except mysql.connector.Error as e:
            op.printLog(logType="CRITICAL", e=e,
                        messageStr="DBManager.query("+str(query)+")")
            traceback.print_exc()
            return None
    
    def insertQuery(self, query):
        initTime = datetime.now(timezone.utc)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            finiTime = datetime.now(timezone.utc)
            count = cursor.rowcount
            op.printLog(logType="STATS",
            messageStr="["+str(count)+"] elements inserted in ["+str(finiTime-initTime)+"] DBManager.insertQuery()")
            cursor.close()
            return self.isSuccess(count)
        except mysql.connector.Error as e:
            op.printLog(logType="CRITICAL", e=e,
                        messageStr="DBManager.insertQuery("+str(query)+")")
            traceback.print_exc()
            return None
    
    def updateQuery(self, query):
        initTime = datetime.now(timezone.utc)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            finiTime = datetime.now(timezone.utc)
            count = cursor.rowcount
            op.printLog(logType="STATS",
            messageStr="["+str(count)+"] elements update in ["+str(finiTime-initTime)+"] DBManager.updateQuery()")
            cursor.close()
            return self.isSuccess(count)
        except mysql.connector.Error as e:
            op.printLog(logType="CRITICAL", e=e,
                        messageStr="DBManager.updateQuery("+str(query)+")")
            traceback.print_exc()
            return None
    
    def deleteQuery(self, query):
        initTime = datetime.now(timezone.utc)
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query)
            self.conn.commit()
            finiTime = datetime.now(timezone.utc)
            count = cursor.rowcount
            op.printLog(logType="STATS",
            messageStr="["+str(count)+"] elements deleted in ["+str(finiTime-initTime)+"] DBManager.deleteQuery()")
            cursor.close()
            return self.isSuccess(count)
        except mysql.connector.Error as e:
            op.printLog(logType="CRITICAL", e=e,
                        messageStr="DBManager.deleteQuery("+str(query)+")")
            traceback.print_exc()
            return None
     
    def isSuccess(self, result):
        if(result==1):
            return True
        return False

    
     
    def tableExist(self, table):
        query = "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'"+str(table)+"')"
        result = self.query(query)
        if(result[0][0] == 1):
            return True
        return False
    
    def fetchAll(self, table, where=None):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.fetchAll("+str(table)+")")
            return None
        
        query = "SELECT * FROM "+str(table) + " "
        if(where != None):
            query+= "WHERE " + where
        result = self.query(query)
        return self.resultsToJSON(result, table)

    def resultsToJSON(self, results, table):
        ## Get elements
        data = list()
        for elem in results: 
            info = dict()
            for index, elemKey in enumerate(self.tables[table]["keys"]["keynames"]):
                info[elemKey]=elem[index]
            data.append(info)
            
        return data
    
    def parseWhere(self, where, table):
        whereString = "WHERE "
        if(where is not None):
            for cond in where:
                if(len(cond) != 3):
                    op.printLog(logType="ERROR",
                        messageStr="Condition needs to have three fields (<key>, <operator ["+str(self.operators)+"]>, <value>) DBManager.parseWhere("+str(table)+","+str(where)+" )")
                    continue
                key = str(cond[0])
                if(key not in self.tables[table]["keys"]):
                    op.printLog(logType="ERROR",
                        messageStr="KEY ["+str(key)+"] not not in table ["+str(table)+"]: DBManager.parseWhere("+str(table)+","+str(where)+" )")
                    continue
                operator = cond[1]
                if(operator not in self.operators):
                    op.printLog(logType="ERROR",
                        messageStr="Operator not allowed : <operator ["+str(self.operators)+"]> DBManager.parseWhere("+str(table)+","+str(where)+" )")
                    continue
                value = cond[2]
                if(type(value) == str):
                    value = "'"+value+"'"
                    
                whereString += key + operator + value
                
        return whereString
    
    def parseSet(self, set, table):
        setString = "SET "
        if(set is not None):
            lenSet = len(set)
            for i, cond in enumerate(set):
                if(len(cond) != 2):
                    op.printLog(logType="ERROR",
                        messageStr="Set needs to have fields (<key>, <newValue>) DBManager.parseSet("+str(table)+","+str(set)+" )")
                    continue
                key = str(cond[0])
                if(key not in self.tables[table]["keys"]):
                    op.printLog(logType="ERROR",
                        messageStr="KEY ["+str(key)+"] not not in table ["+str(table)+"]: DBManager.parseWhere("+str(table)+","+str(set)+" )")
                    continue
                
                value = cond[1]
                if(type(value) == str):
                    value = '"'+value+'"'
                    
                setString += key + "=" + str(value) + ","
                
        return setString
    
    def getIdValueList(self, id, value, table):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.getIdValueList("+str(table)+")")
            return None
        if(id not in self.tables[table]["keys"]["keynames"] or value not in self.tables[table]["keys"]["keynames"]):
            op.printLog(logType="ERROR",
                        messageStr="The id or values are not fields form ["+str(table)+"] VALID KEYS: "+str(self.tables[table]["keys"]["keynames"])+" DBManager.getIdValueList("+str(table)+")")
            return None
            
        ids=list()
        for elem in self.fetchAll(table):
            ids.append((elem[id],elem[value]))
        return ids
    
    def getValueIdDict(self, id, value, table):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.getIdValueList("+str(table)+")")
            return None
        if(id not in self.tables[table]["keys"]["keynames"] or value not in self.tables[table]["keys"]["keynames"]):
            op.printLog(logType="ERROR",
                        messageStr="The id or values are not fields form ["+str(table)+"] VALID KEYS: "+str(self.tables[table]["keys"]["keynames"])+" DBManager.getIdValueList("+str(table)+")")
            return None
            
        values=dict()
        for elem in self.fetchAll(table):
            values[elem[value]] = elem[id]
        return values

    def insertTableElement(self, elem, table):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.insertTableElement("+str(table)+")")
            return None
        
        query = "INSERT INTO "+str(table)+" "+str(tuple(self.tables[table]["keys"]["keynames"])).replace("'id', ", "").replace("'","`")+" VALUES "+ str(elem)
        result = self.insertQuery(query)
        return result

    def insertTableElementWithId(self, ignore, elem, table):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.insertTableElement("+str(table)+")")
            return None
        
        query = "INSERT INTO "+str(table)+" "+str(tuple(self.tables[table]["keys"]["keynames"])).replace("'"+str(ignore)+"', ", "").replace("'","`")+" VALUES "+ str(elem)
        result = self.insertQuery(query)
        return result
    
    def deleteTableElement(self, table, where):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.addElementToTable("+str(table)+")")
            return None
        
        query = "DELETE FROM "+table+" WHERE " + where
        result = self.deleteQuery(query)
        return result
    
    def updateTableElement(self, table, set, where=None):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.addElementToTable("+str(table)+")")
            return None
        setString = self.parseSet(set, table)
        query = 'UPDATE '+str(table) +' '+ str(setString) + 'updated_at="' + str(datetime.now()) + '"'
        if(where!=None):
            query+= " WHERE " + str(where)
        result = self.updateQuery(query)
        return result

    def resetIndex(self, table):
        if(not self.tableExist(table)):
            op.printLog(logType="ERROR",
                        messageStr="Table not Exists. DBManager.addElementToTable("+str(table)+")")
            return None
        self.query("SET  @num := 0;")
        self.updateQuery('UPDATE '+str(table)+' SET id = @num := (@num+1);')
        result =self.updateQuery('ALTER TABLE '+str(table)+' AUTO_INCREMENT = 1;')
        return result

    
if __name__ == '__main__':
    dbManager = DBManager()
    if(dbManager.checkIfConnected()):
        time = str(datetime.now())
        #print(dbManager.insertTableElement(elem=("SUV", "250","350", "150", time, time), table='TipoVehiculo'))
        #print(dbManager.insertTableElement(elem=("Furgoneta", "300","380", "200", time, time), table='TipoVehiculo'))
        #values = dbManager.getValueIdDict(id="id", value="nombre", table="TipoVehiculo")
        #print(values)
        dbManager.query()
        #dbManager.resetIndex(table="TipoVehiculo")
        #dbManager.deleteTableElement(table="TipoVehiculo", where="id = "+str(values["SUV"]))
        #print(dbManager.insertTableElement(elem=("1247-LDG",1,time, time), table='Vehiculo'))
    else:
        print("Is not connected!")
        
