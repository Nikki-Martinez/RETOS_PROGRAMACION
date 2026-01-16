# Hacer un programa que pida tres números al usuario y muestre por pantalla 
# cuál es el mínimo y cuál es el máximo y que indique si son pares o impares. 
# No usar listas.
n1 = int(input("Ingresa el primer número entero: "))
n2 = int(input("Ingresa el segundo número entero: "))
n3 = int(input("Ingresa el tercer número entero: "))

print(f"\nEl número mayor es: {max(n1, n2, n3)}")
print(f"El número menor es: {min(n1, n2, n3)}\n")


for n in (n1, n2, n3):
    if n % 2 == 0:
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")