import sqlite3

class Work_Database:
    def __init__(self, database) -> None:
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        
        
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE users (
            telegram_id INT
            username TEXT, 
            fullname TEXT    
        )""")
    
    def insert_users(self, telegram_id, username, fullname):
        self.cursor.execute(f"""
        INSERT INTO users
        VALUES (?, ?, ?)""", (telegram_id, username, fullname))
        self.connection.commit()
        
        # update users qoshish
        
    def update_users_all_info(self, id, new_username, new_fullname):
        self.cursor.execute("""UPDATE users SET username = ?, fullname = ? WHERE telegram_id = ?""", (new_username, new_fullname, id))
        self.connection.commit()
        
    def update_users_username(self, id, new_username):
        self.cursor.execute("""UPDATE users SET username = ? WHERE telegram_id = ?""", (new_username, id))
        self.connection.commit()
        
    def update_users_fullanme(self, id, new_fullname):
        self.cursor.execute("""UPDATE users SET fullname = ? WHERE telegram_id = ?""", (new_fullname, id))
        self.connection.commit()