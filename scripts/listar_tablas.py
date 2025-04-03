

##listar_tablas


import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path="config/.env")

def conectar_postgresql():
    """Establece conexión con PostgreSQL."""
    conexion = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conexion

def listar_tablas():
    """Consulta y muestra las tablas disponibles en la base de datos."""
    conexion = conectar_postgresql()
    cursor = conexion.cursor()
    
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
    )
    tablas = cursor.fetchall()
    
    if tablas:
        print("📌 Tablas disponibles en la base de datos:")
        for tabla in tablas:
            print(f" - {tabla[0]}")
    else:
        print("⚠️ No se encontraron tablas en la base de datos.")

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    print("🔍 Buscando tablas en la base de datos...")
    listar_tablas()
