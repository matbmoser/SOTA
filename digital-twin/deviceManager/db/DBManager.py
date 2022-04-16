from dbConfig import dbConfig
import mysql.connector


class DBManager():
    def __init__(self):
        self.conn = None
        self.tables = None
        try:
            connection = mysql.connector.connect(host=dbConfig.hostname,
                                                 database=dbConfig.dbname,
                                                 user=dbConfig.username,
                                                 password=dbConfig.password)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                self.conn = connection
                self.getAllTables()
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

    def checkIfConnected(self):
        if self.conn.is_connected():
            return True
        return False

    def getAllTables(self):
        self.tables = list()
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = '" + \
            str(dbConfig.dbname)+"';"
        print(query)
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for table in result:
            self.tables.append(table[0])
        return self.tables
    

if __name__ == '__main__':
    dbManager = DBManager()
    if(dbManager.checkIfConnected()):
        print("Is connected!")
        dbManager.getAllTables()
        print(dbManager.tables)
    else:
        print("Is not connected!")
