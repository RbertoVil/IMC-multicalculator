from flask import Flask, render_template, request
import functions

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/results", methods=["POST"])
def results():
    name = request.form.get("name")
    weight = float(request.form.get("weight"))
    height = float(request.form.get("height"))

    aplicarIMC = functions.IMC(name, weight, height)
    resultadoIMC = aplicarIMC[0]
    composicionCorporal = aplicarIMC[1]

    functions.crearPDF(1)

    return render_template("results.html", nombre=name, peso=weight, estatura=height, resultadoIMC=resultadoIMC, composicionCorporal=composicionCorporal)

@app.route("/download")
def download():
    # Descargar el PDF

    flask.send_file("pdf/resultado-IMC.pdf")

    return render_template("download.html")
