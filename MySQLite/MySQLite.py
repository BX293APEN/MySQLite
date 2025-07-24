import os, sqlite3

class MySQLite():
    def __init__(self, db = f"{os.path.dirname(__file__)}/sqlite3.db"):
        self.databaseHost = sqlite3.connect(database = db) # データベースとの接続
    
    def __enter__(self):
        self.database = self.databaseHost.cursor() # カーソルを作る
        return self
    
    def send_sql(self, sql): # SQL文送信
        self.database.execute(sql)
        self.db_commit()
        return self.database.fetchall() # タプル形式で全て取得
    
    def db_commit(self):
        self.databaseHost.commit()

    def __exit__(self, *args):
        self.db_commit()
        self.database.close()
        self.databaseHost.close()
        

class SQLiteDebug(MySQLite):
    def __init__(self, db = f"{os.path.dirname(__file__)}/sqlite3.db"):
        self.db = db
        super().__init__(self.db)
    
    def db_remove(self):
        os.remove(self.db)
    
    def db_console(self):
        self.sql = ""
        sqlLine = " "
        while (
            (sqlLine.count(";") == 0) and
            (sqlLine != "") and
            (sqlLine.count("quit") == 0)
        ):
            sqlLine = input("sqlite > ")
            self.sql += f" {sqlLine}"
        
        if (self.sql.count("quit") > 0):
            return ["Bye"]
        else:
            return self.send_sql(self.sql)

def main():
    val = ""
    while (val != ["Bye"]):
        with SQLiteDebug(f"{os.getcwd()}/sqlite3.db") as db:
            try:
                val = db.db_console()
                if len(val) != 0:
                    print(val)
            except Exception as e:
                print(e)
