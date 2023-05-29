def calculadora_dni(numero_dni):
    letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J",	"Z", "S", "Q", "V", "H", "L", "C", "K",	"E"]
    cantidad_letras = len(letras)

    return letras[numero_dni % cantidad_letras]
