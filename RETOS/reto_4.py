#Uso de condiciones y listas
numeros = []
#Se solicita ingresar 10 numeros enteros, en vez de declarar 10 variables, se usa una condición que vaya creando cada variable para cada número ingresado y se almacene en una lista.
for i in range(1, 11):
    numero = int(input(f"Ingrese un número entero para #{i}: "))
    numeros.append(numero)

for num in numeros:
    #usamos concatenación para crear el mensaje inicial con el número
    mensaje = str(num) 
    #uso de condiciones para determinar si el número es negativo o duplicado
    if num < 0:
        mensaje += " - negativo"

    if numeros.count(num) > 1:
        mensaje += " - duplicado"

    print(mensaje)
