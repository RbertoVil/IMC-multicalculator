from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class persona:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.peso = ""
        self.estatura =""
        self.resultadoIMC = ""
        self.composicionCorporal =""


def IMC(nombrePersona, peso, estatura):
    # Determinar el IMC de una persona
    # Y la composicion corporal
    denominador = estatura ** 2
    resultadoIMC = peso / denominador

    if resultadoIMC <= 18.5:
        composicionCorporal = "Peso inferior al normal."
    elif resultadoIMC > 18.5 and resultadoIMC <= 24.9:
        composicionCorporal = "Peso normal."
    elif resultadoIMC > 24.9 and resultadoIMC <= 29.9:
        composicionCorporal = "Peso superior al normal."
    else:
        composicionCorporal = "Obesidad."

    return(resultadoIMC, composicionCorporal)


def crearPDF(nroCols):
    # Crearemos el PDF
    archPDF = canvas.Canvas("./pdf/resultado-IMC.pdf", pagesize=letter)

    xInvertido, y = letter	# coordenadas

    archPDF.drawString(200, y - 50, "República Bolivariana de Venezuela")
    archPDF.drawString(200, y - 64, "Universidad Nacional Experimental")
    archPDF.drawString(200, y - 78, "de los Llanos Occidentales")
    archPDF.drawString(200, y - 92, "\"Ezequiel Zamora\"")
    archPDF.drawString(200, y - 106, "Unellez - Edo. Barinas")

    archPDF.drawImage("./img/Unellezlogotipo.jpg", 50, y - 110, width=80, height=80)

    # Creamos cuadro
    xlist = [60, 250, 280, 310, 360, xInvertido - 60]	
	
    ylist = [y - 120, y - 136, y - 152, y - 168, y -184, y - 200, y - 216, y - 232, y - 248, y - 264, y - 280, y - 296, y - 312, y - 328, y - 344, y - 360, y - 376, y - 392, y - 408, y - 424, y - 440, y - 456]

    archPDF.grid(xlist, ylist)

    # Footer
    archPDF.drawString(xInvertido/3, 50, "Developed by Roberto Villasana & Luis Rivas")

    # Guardamos la página actual
    archPDF.showPage()

    print("¿creando pdf?")

    # Guardamos el archivo creado
    archPDF.save()

    print("¿save pdf?")
