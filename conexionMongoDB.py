from pymongo import MongoClient
from datetime import datetime
import json

# establish connex
conn = MongoClient('localhost', 27017)
conn = MongoClient()

# create db
db = conn.baseDeDatos

# create collection
collection = db.datosNodemcu

# <-------------------------------------------------------- INSERT 
# Funciones para insertar datos
def insertDatos(DataconFecha) :
    """
    Una vez que se agrego fecha y hora en la NBDataconFecha recibida por POST
    agregamos el documento "registro"  en la base de datos.
    """
    insertData = collection.insert(DataconFecha)

def showData() :
    #return [ a for a in collection.find()]
    return collection.find()

def showD() :
    return [ a for a in collection.find()]