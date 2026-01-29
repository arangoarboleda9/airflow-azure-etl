from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
# Añadimos la ruta de los scripts para que Airflow los encuentre
sys.path.append('/opt/airflow/scripts')

# Importamos la función del archivo que creamos en el Paso 4
from etl_script import ejecutar_proceso

# Configuración básica del DAG
default_args = {
    'owner': 'alejandro',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='etl_azure_v1',
    default_args=default_args,
    description='Mi primer pipeline de API a Azure SQL',
    schedule=None, # Lo activaremos manualmente para probar
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['proyecto_ingenieria'],
) as dag:

    # Tarea única: ejecutar el script de Python
    tarea_etl = PythonOperator(
        task_id='run_etl_script',
        python_callable=ejecutar_proceso
    )

    tarea_etl # type: ignore