import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}


def db_conn():

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def close_conn(connection):
    """
    Cierra la conexión a la base de datos si está activa.
    """
    if connection and connection.is_connected():
        connection.close()


def execute_query_db(connection, sql_file_path, params=None):
    with open(sql_file_path, "r") as file:
        sql = file.read()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results
