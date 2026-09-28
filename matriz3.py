#Suma de matrices A y B

matrizA = []
matrizB = []
matrizSuma = []

# Pedir los datos de la matriz A
for i in range(3):
    matrizA.append([])
    for j in range(3):
        valor = int(input(f"Matriz A [{i + 1}][{j + 1}]: "))
        matrizA[i].append(valor)

# Pedir los datos de la matriz B
for i in range(3):
    matrizB.append([])
    for j in range(3):
        valor = int(input(f"Matriz B [{i + 1}][{j + 1}]: "))
        matrizB[i].append(valor)

# Suma de matrices A y B
for i in range(3):
    matrizSuma.append([])
    for j in range(3):
        suma_posicion = matrizA[i][j] + matrizB[i][j]
        matrizSuma[i].append(suma_posicion)

# Mostrar el resultado de la suma
print("\n=== Matriz Resultante (A + B) ===")
for fila in matrizSuma:
    print(fila)