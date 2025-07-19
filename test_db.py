# test_db.py
from app.core.database import Database

db = Database()
result = db.search("capital of France")
print(result)  # Debería imprimir ('Paris',)
db.close()