n1 = int(input("Ingresa el primer número entero: "))
n2 = int(input("Ingresa el segundo número entero: "))   
n3 = int(input("Ingresa el tercer número entero: "))
print("El número mayor es:", max(n1, n2, n3))
print("El número menor es:", min(n1, n2, n3))
if n1 % 2 == 0:
    print(f"El número {n1} es par")
else:
    print(f"El número {n1} es impar")
if n2 % 2 == 0:
    print(f"El número {n2} es par")
else:
    print(f"El número {n2} es impar")
if n3 % 2 == 0:
    print(f"El número {n3} es par")
else:
    print(f"El número {n3} es impar")