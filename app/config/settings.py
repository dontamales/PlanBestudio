from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

# Obtener variables de entorno, lanzar error si no están definidas
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Validar que todas las variables estén presentes
if not all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    raise ValueError("Faltan variables de entorno en .env. Revisa DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT.")

DATABASE_CONFIG = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'port': DB_PORT
}