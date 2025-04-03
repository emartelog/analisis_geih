# 📁 scripts/

Esta carpeta contiene los módulos funcionales del proyecto de análisis de la GEIH. Aquí se agrupan las piezas clave del proceso ETL, análisis y exploración.

## 🗂️ Estructura de Scripts

| Archivo              | Descripción |
|----------------------|-------------|
| `conexion.py`        | Módulo para conectarse a la base de datos PostgreSQL usando SQLAlchemy y variables de entorno. |
| `extraer_datos.py`   | Prueba la conexión a la base y extrae registros de una tabla para verificar funcionamiento. |
| `listar_tablas.py`   | Lista todas las tablas disponibles en el esquema público de PostgreSQL. Útil para exploración inicial. |
| `procesar_datos.py`  | Realiza análisis exploratorio (EDA) básico y visualización de distribuciones. Puede exportar CSV. |

> Todos los scripts están pensados para ser usados de forma individual o integrados dentro del pipeline completo.

## 🔧 Dependencias

Asegúrate de tener estas bibliotecas instaladas en tu entorno:

- pandas
- sqlalchemy
- psycopg2
- python-dotenv
- matplotlib
- seaborn