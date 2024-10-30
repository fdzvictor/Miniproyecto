
import psycopg2

def conectar_bbdd(bbdd_name, postgres_pass, user, host="localhost"):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=postgres_pass,
        
    )
    connection.autocommit = True
    return connection