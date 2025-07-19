import psycopg2
from app.config.settings import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor()

    def search(self, text):
        self.cursor.execute("SELECT answer_text FROM questions WHERE question_text ILIKE %s", (f"%{text}%",))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()