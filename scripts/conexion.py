### Script 1: Conectar y verificar conexión a PostgreSQL

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv("config/.env")

print("🚀 Iniciando conexión a PostgreSQL...")  # Nuevo mensaje antes de conectar

def conectar_postgresql():
    try:
        # Obtener variables de entorno
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")

        # Validar que todas las variables estén definidas
        if not all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
            raise ValueError("❌ Error: Faltan variables de entorno en config/.env")

        # Crear conexión con SQLAlchemy
        DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(DATABASE_URL)

        print("✅ Conexión exitosa a PostgreSQL")
        return engine
    except Exception as e:
        print(f"❌ Error al conectar con PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    conectar_postgresql()


