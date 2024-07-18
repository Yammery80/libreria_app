import psycopg2
from psycopg2 import pool

#Crear un pol de conexiones
connection_pool = pool.SimpleConnectionPool(
    1, 20,
    database="biblioteca",
    user="postgres",
    password="Lindel2005",
    host="localhost",
    port="5432"
    )
def conectar():
    return connection_pool.getconn()
def desconectar(conn):
    connection_pool.putconn(conn)