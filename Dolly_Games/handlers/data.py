import sqlite3 as sq

class Database:
    def __init__(self):
        self.db = sq.connect('handlers/players.db')
        self.cursor = self.db.cursor()

    def get_balance(self, id):
        query = 'SELECT dolly FROM users WHERE id = ?'
        params = (id, )
        result = self.cursor.execute(query, params).fetchone()
        return result[0] if result is not None else None
    
    def insert_user(self, id):
        query = "INSERT INTO users (id) VALUES (?)"
        params = (id, )
        self.cursor.execute(query, params)
        self.db.commit()
        
    def update_balance(self, id, dolly):
        query = 'UPDATE users SET dolly = ? WHERE id = ?'
        params = (dolly, id)
        self.cursor.execute(query, params)
        self.db.commit()

    def get_minti(self, id):
        query = 'SELECT minti FROM users WHERE id = ?'
        params = (id, )
        result = self.cursor.execute(query, params).fetchone()
        return result[0] if result is not None else None