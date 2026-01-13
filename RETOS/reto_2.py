n = int(input("Ingresa un número entero entre 10 y 20: "))

if n < 10 or n > 20:
    print("El numero ingresado no esta en el rango entre 10 y 20")
else:
    for i in range(1, n+1):
        print(i)
    for i in range(31, n, -1):
        print(i)