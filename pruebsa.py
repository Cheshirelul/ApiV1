#from pymongo import MongoClient
import pymongo
from datetime import datetime
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["baseDeDatos"]
mycol = mydb["datosNodemcu"]# establish connex


#def showData():
 #   mycol.find()
        #print(x) 
        

for x in mycol.find():
  print(x) 

#print(showData())