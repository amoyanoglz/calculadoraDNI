from calculadora_dni import calculadora_dni

def dameUnNum():
    msg = "Dame un numero "
    entrada = ''
    invalido = False
    num = -1
    while not entrada.isnumeric() or num >= 99999999 or num < 0:
        if invalido:
            print("obligatorio número")
        invalido = True
        entrada = input(msg)
    num = int(entrada)

    return int(num)

numero_dni = dameUnNum()
# numero_dni = int(input("dame número de DNI"))
letra_dni = calculadora_dni(numero_dni)
print(f"dni calculado {numero_dni} - {letra_dni}")