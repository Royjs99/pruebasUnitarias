import mysql
import mysql.connector


def conexion():
    config = {
        "user": "rodrigo",
        "password": "Wipaki83_",
        "host": "34.28.131.85",
        "database": "posgrado",
    }
    conexion = mysql.connector.connect(**config)
    return conexion


class BaseDeDatos:
    _instance = None

    def __init__(self):
        self.conn = conexion()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseDeDatos, cls).__new__(cls)    
        return cls._instance
