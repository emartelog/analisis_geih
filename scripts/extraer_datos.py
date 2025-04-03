import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.conexion import conectar_postgresql
import pandas as pd

def extraer_datos():
    """Extrae datos de la tabla y los muestra."""
    print("📥 Iniciando extracción de datos...")

    try:
        engine = conectar_postgresql()
        query = 'SELECT * FROM "DATOS_DE_LA_VIVIENDA_GEIH" LIMIT 5;'
        
        df = pd.read_sql(query, con=engine)  # Usa SQLAlchemy correctamente
        print("✅ Datos extraídos con éxito:")
        print(df)
        
    except Exception as e:
        print(f"❌ Error al extraer datos: {e}")

extraer_datos()
