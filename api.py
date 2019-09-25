from flask import Flask, jsonify, render_template
from flask import request
from datetime import datetime
import conexionMongoDB
print ('you are here')
app = Flask(__name__)

@app.route("/")
def hello():
        return "First Flask APP"
#==============================================================
#Método para postear un json
#No diseñada para dar información, es para recibir
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print ('Getting RAW Data')
    print (request.get_data())
    print ('Validate JSON Format')
    print (request.is_json)
    content = request.get_json()
    # Registro la fecha desde el lado del servidor
    content.update({"FECHA":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    print (content)
    conexionMongoDB.insertDatos(content)
    return 'JSON posted'

@app.route('/showData', methods = ['GET'])
def prueba():
        #print(conexionMongoDB.showData())
        #return "Aqui se mostraran los datos de la BD"
        #myData = conexionMongoDB.showData()
        #print(myData)
        datosNodemcu = conexionMongoDB.collection.find()
        #print(datos)
        return render_template("log.html", datosNodemcu = datosNodemcu)

#--------------------------------------- este es para pruebas
@app.route('/mostrar', methods = ['GET'])
def prueba2():
        #print(conexionMongoDB.showData())
        #return "Aqui se mostraran los datos de la BD"
        #myData = conexionMongoDB.showData()
        #print(myData)
        datosNodemcu2 = [doc for doc in conexionMongoDB.collection.find({},{"_id":0})]
        #print(datos)
        return jsonify(datosNodemcu2)