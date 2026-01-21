#Calcular factorial de N, ya sea por un solo numero ingresado o por cada numero dentro de una lista


#uso de funcion para reutilización
def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i
        return fact
        
n = int(input("Ingrese el número para sacarle factorial: "))
print(f"El factorial de {n} es {factorial(n)}")

numeros = [5, 7, 9]
#uso de metodos
for n in numeros:
    #Metodo join() para unir cadenas usando separadores
    pasos = " * ".join(str(i) for i in range(n, 0, -1))
    resultado = factorial(n)
    print(f"{n}! = {pasos}, factorial: {resultado}")

