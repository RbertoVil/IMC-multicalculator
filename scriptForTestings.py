import functions
import pprint
import os

def pruebaClases():
    estudiante = functions.persona()

    estudiante.id = "estudiante1"
    estudiante.name = "Roberto"
    estudiante.peso = 70
    estudiante.estatura = 1.75
    print(estudiante)

    pprint.pprint(dir(estudiante))

    print(estudiante.id)

def listarArch():
    os.listdir("pdf/")

#functions.crearPDF(2)

#pruebaClases()
