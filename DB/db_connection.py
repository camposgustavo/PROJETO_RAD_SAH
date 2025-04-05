import mysql.connector 

#criar classe de conexao ao db
class DatabaseConnection:
    def __init__(self):
        self.host="localhost"
        self.usernarme="admin"
        self.password="root"
        self.db="hotel_db"
        self.connection=self.db_connection()

    #criar a conexao
    def db_connection(self):
        return mysql.connector.connect(
            host=self.host,
            username=self.username,
            password=self.password,
            db=self.db,
        )
        
    def CreateDB (self,cursor):
        cursor=self.connection.cursor()
        cursor.execute('CREATE DATABASE hotel_db IF NOT EXISTS, USE hotel_db')
        cursor.close()
