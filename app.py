from flask import Flask, render_template, request
import functions

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/results", methods=["POST","GET"])
def results():
    nombre = request.form.get("name")
    peso = request.form.get("weight")
    estatura = request.form.get("height")

    aplicarIMC = functions.IMC(nombre, peso, estatura)
    resultadoIMC = aplicarIMC[0]
    composicionCorporal = aplicarIMC[1]
    return render_template("results.html", nombre=nombre, peso=peso, estatura=estatura, resultadoIMC=resultadoIMC, composicionCorporal=composicionCorporal)

