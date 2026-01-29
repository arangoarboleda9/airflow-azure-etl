import pandas as pd
import requests
import sqlalchemy
import urllib
import logging

def ejecutar_proceso():
    # 1. EXTRACCIÓN
    logging.info("Iniciando extracción desde la API...")
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        r = requests.get(url)
        r.raise_for_status() # Verifica si la API respondió bien
        df = pd.DataFrame(r.json())
        logging.info(f"Se extrajeron {len(df)} registros.")
    except Exception as e:
        logging.error(f"Error en extracción: {e}")
        raise

    # 2. TRANSFORMACIÓN
    logging.info("Transformando datos...")
    # Limpieza básica
    df = df[['id', 'title', 'body']]
    df['title'] = df['title'].str.upper() # Títulos en mayúsculas
    df['fecha_carga'] = pd.Timestamp.now() # Auditoría

    # 3. CARGA A AZURE SQL
    logging.info("Conectando a Azure SQL...")
    
    # --- REEMPLAZA ESTOS DATOS CON LOS DE TU PORTAL DE AZURE ---
    import os
    server = os.getenv('AZURE_SERVER')
    database = os.getenv('AZURE_DB')
    username = os.getenv('AZURE_USER')
    password = os.getenv('AZURE_PASSWORD')
    
    # Configuramos el driver para SQL Server
    params = urllib.parse.quote_plus( # type: ignore
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={server};DATABASE={database};'
        f'UID={username};PWD={password};'
        'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    )
    
    conn_str = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = sqlalchemy.create_engine(conn_str)
    
    try:
        # Cargamos a la tabla 'reporte_posts'
        df.to_sql('reporte_posts', engine, if_exists='replace', index=False)
        logging.info("¡Carga exitosa en Azure!")
    except Exception as e:
        logging.error(f"Error cargando a Azure: {e}")
        raise

if __name__ == "__main__":
    ejecutar_proceso()