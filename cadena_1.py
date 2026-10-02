vector = ["j", "u", "a", "n"]
print(type(vector))


for letra in vector:
    print(letra)

nombre= "Luis"
print("*"*13)
for letra in nombre:
    print(letra)

print(len(vector))
print(len(nombre))

def convertirAMayuscula(texto):
    return f"{texto.upper()}"

def convertirAMinuscula(texto):
    return f"{texto.lower()}"

def capitalizar(texto):
    return f"{texto.capitalize()}"

def titulo(texto):
    return f"{texto.title()}"

def generarGmail(texto):
    nombre = texto.split()
    email = "".join(palabra[:3].lower() for palabra in nombre)
    return f"{email}@uamv.edu.ni"

print(convertirAMayuscula(nombre))
#print(convertirAMayuscula(vector))

for each in vector:
    print(convertirAMayuscula(each), end="")

print()
print(convertirAMinuscula(nombre))
print(titulo(nombre))
print(generarGmail("Justin Leandro Ruiz Madrigal"))