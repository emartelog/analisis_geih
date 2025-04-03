import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Conectar a PostgreSQL y cargar los datos
def cargar_datos(query, conexion_str):
    """Carga los datos desde PostgreSQL ejecutando una consulta SQL."""
    engine = create_engine(conexion_str)
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

# Exploración inicial
def explorar_datos(df, nombre_tabla):
    """Realiza un análisis exploratorio de datos básico."""
    print(f"\n📌 Información general de la tabla: {nombre_tabla}\n")
    print(df.info())
    
    print("\n📊 Descripción estadística:\n")
    print(df.describe(include='all'))
    
    print("\n🔍 Valores nulos por columna:\n")
    print(df.isnull().sum())
    
    print("\n🆔 Valores duplicados:", df.duplicated().sum())

# Visualización de distribuciones
def visualizar_datos(df, nombre_tabla):
    """Genera histogramas y un mapa de calor de correlaciones."""
    plt.figure(figsize=(12, 6))
    df.hist(bins=30, figsize=(12, 10), edgecolor='black')
    plt.suptitle(f"Distribución de variables numéricas - {nombre_tabla}")
    plt.show()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title(f"Mapa de calor de correlaciones - {nombre_tabla}")
    plt.show()

# Guardar datos en CSV (opcional)
def guardar_csv(df, nombre_archivo):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(nombre_archivo, index=False, encoding='utf-8')
    print(f"📁 Datos guardados en {nombre_archivo}")

if __name__ == "__main__":
    conexion_str = "postgresql://usuario:password@localhost:5432/geih"  # Modificar con credenciales reales
    tablas = [
        "caracteristicas_generales",
        "datos_hogar_vivienda",
        "fuerza_de_trabajo",
        "migracion",
        "no_ocupados",
        "ocupados",
        "otras_formas_trabajo",
        "otros_ingresos_impuestos"
    ]
    
    for tabla in tablas:
        print(f"\n🔹 Procesando tabla: {tabla}\n")
        query = f"SELECT * FROM {tabla};"
        df = cargar_datos(query, conexion_str)
        explorar_datos(df, tabla)
        visualizar_datos(df, tabla)
        
        # Guardar una copia en CSV si se necesita
        # guardar_csv(df, f"{tabla}.csv")

