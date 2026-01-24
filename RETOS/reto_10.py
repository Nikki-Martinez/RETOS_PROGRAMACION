#Haz un programa en Python que pida dos números enteros N y M al usuario.
#Calcula y muestra por pantalla el máximo común divisor (MCD) de N y M.
#Calcula y muestra por pantalla el mínimo común múltiplo (MCM) de N y M.
#Hacer lo mismo pero pidiendo varios números al usuario. Almacénalos en una lista y calcula el MCM y el MCD de todos ellos.

def calcular_mcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calcular_mcd(a, b)

# 1. Pedir números al usuario
numeros = []
print("Calculadora de MCD y MCM de una lista")
print("Introduce números enteros. Introduce el 0 para terminar y calcular.")

while True:
    try:
        entrada = int(input("Introduce un número: "))
        
        # Si el usuario introduce 0, salimos del bucle
        if entrada == 0:
            break
            
        numeros.append(entrada)
    except ValueError:
        print("Error: Por favor, introduce solo números enteros.")

if len(numeros) < 2:
    print("Se necesitan al menos dos números para calcular.")
else:
    
    resultado_mcd = numeros[0]
    resultado_mcm = numeros[0]

    
    for i in range(1, len(numeros)):
        resultado_mcd = calcular_mcd(resultado_mcd, numeros[i])
        resultado_mcm = calcular_mcm(resultado_mcm, numeros[i])

   #Mostrar resultados  
    print("-" * 20)
    print(f"Lista: {numeros}")
    print(f"MCD total: {resultado_mcd}")
    print(f"MCM total: {resultado_mcm}")
    