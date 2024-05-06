import sqlite3

class SELECT:
    def __init__(self, file_sql, file_db) -> None:
        self.file_sql = file_sql
        self.file_db = file_db

    def select(self) -> list:
        with sqlite3.connect(self.file_db) as con:
                cur = con.cursor()
                cur.execute(self.create_db())
                return cur.fetchall()
        
    def create_db(self):
                
        # читаємо файл зі скриптом для створення БД
        with open(self.file_sql, 'r') as f:
            sql = f.read()
        return sql
    
   

if __name__ == "__main__":
    p = SELECT("query_2.sql","salary.db")
    print(p.select())