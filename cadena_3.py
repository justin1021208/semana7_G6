#Leer una cadena de texto y buscar una letra o texto

def buscar(valor, cadena):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return "Se encontró el valor buscado"

    else:
        return "No se encontró el valor buscado"

def saberSiContiene(cadena, valor):
    return valor in cadena

cadena = input("Dime una frase: ")
valor = input("Dime el dato a buscar: ")

print(buscar(valor, cadena))
print(saberSiContiene(cadena, valor))