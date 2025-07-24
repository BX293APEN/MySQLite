import os, sqlite3, copy

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
        while True:
            sql = input("sqlite3 > ")
            while True:
                self.sql += f"{sql} "
                if sql.count(";") > 0 or sql == "":
                    sql = copy.deepcopy(self.sql)
                    self.sql = ""
                    break
                sql = input("    - > ")
                
            if sql.count("quit") > 0:
                return ["Bye"]
            else:
                return self.send_sql(sql)
            
def main():
    val = ""
    while True:
        with SQLiteDebug(f"{os.getcwd()}/sqlite3.db") as db:
            try:
                val = db.db_console()
                if val != ["Bye"]:
                    for rd in val:
                        print(rd)
                else:
                    break
            except Exception as e:
                print(e)
