# 🚀 Azure Data Pipeline ETL con Apache Airflow

Este proyecto implementa un pipeline de datos (ETL) automatizado que extrae información de una API REST pública, realiza transformaciones de limpieza con Pandas y carga los resultados en una base de datos **Azure SQL Database**. Todo el entorno está orquestado mediante **Apache Airflow** corriendo en contenedores **Docker**.

## 🛠️ Stack Tecnológico
* **Orquestador:** Apache Airflow 3.1.6
* **Lenguaje:** Python 3.12
* **Procesamiento:** Pandas & SQLAlchemy
* **Base de Datos:** Azure SQL Database
* **Infraestructura:** Docker & Docker Compose
* **Driver de Conexión:** ODBC Driver 18 for SQL Server

## 📈 Arquitectura del Pipeline
1. **Extract:** Llamada a JSONPlaceholder API para obtener datos de posts.
2. **Transform:** Limpieza de datos, renombrado de columnas y validación de tipos con Pandas.
3. **Load:** Inserción de datos en Azure SQL mediante una conexión segura por ODBC.

## 🚀 Configuración del Proyecto

### Requisitos previos
* Docker y Docker Compose instalados.
* Cuenta de Microsoft Azure con una SQL Database activa.

### Instalación
1. Clona este repositorio.
2. Configura tus credenciales de Azure en `scripts/etl_script.py`.
3. Levanta el entorno de Airflow:
   ```bash
   docker compose up -d
Accede a la interfaz de Airflow en http://localhost:8080.

⚙️ Variables de Entorno
El archivo docker-compose.yaml incluye la variable _PIP_ADDITIONAL_DEPENDENCIES para instalar automáticamente las librerías necesarias:

pandas

requests

sqlalchemy

pyodbc


---

### 2. Cómo subirlo a GitHub desde la terminal de VS Code

Sigue estos comandos uno por uno para crear tu repositorio:

#### A. Preparar el repositorio local
```bash
# Inicializa el repositorio de Git
git init

# Añade todos los archivos (asegúrate de que no se suban contraseñas reales)
git add .

# Crea el primer commit
git commit -m "Primer commit: Pipeline ETL Airflow a Azure"

👤 Autor
Alejandro Arango - Data Engineering
