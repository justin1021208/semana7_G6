#Matriz 2 x 2
matrizA = []
matrizB = []
matrizC = []

print("Ingrese los valores de la primer matriz 2x2: ")
for i in range (2):
    fila = []
    for j in range (2):
        valor = float(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
        fila.append(valor)
    matrizA.append(fila)

print("Ingrese los valores de la matriz 2x2: ")
for i in range (2):
    fila = []
    for j in range (2):
        valor = float(input(f"Ingrese el valor de la posición ({i+1},{j+1})"))
        fila.append(valor)
    matrizB.append(fila)

#Multiplicación de matrices
for i in range (2):
    fila = []
    for j in range (2):
        suma = 0
        for k in range (2):
            suma += matrizA [i][k] * matrizB [k][j]
        fila.append(suma)
    matrizC.append(fila)

print("La matriz resultante es: ")
for fila in matrizC:
    print(fila)