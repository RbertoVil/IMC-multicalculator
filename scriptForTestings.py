import functions
import pprint

def pruebaClases():
    estudiante = functions.persona()

    estudiante.id = "estudiante1"
    estudiante.name = "Roberto"
    estudiante.peso = 70
    estudiante.estatura = 1.75
    print(estudiante)

    pprint.pprint(dir(estudiante))

    print(estudiante.id)

#functions.crearPDF(2)

#pruebaClases()
