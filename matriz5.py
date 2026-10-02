"""
Dada una matriz de identidad nxn 
Mostar en color azul solo la diagonal de 1
"""

from colorama import Fore, Style

n = int(input("Ingrese dimensiones de la matriz: "))
matriz = []

# Creamos la matriz identidad
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

#Imprimimos mostrando la diagonal en azul
for i in range(n):
    for j in range(n):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()