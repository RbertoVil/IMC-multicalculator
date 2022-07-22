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
