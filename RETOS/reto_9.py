#Hacer una función que reciba una lista y devuelva una lista sin repetidos.
def quitar_repetidos():
    lista = []
    lista_sin_repetidos = []

    num = -1

    while num != 0:
        num = int(input("Ingrese un numero: "))
        if num == 0:
            break
        lista.append(num)

    for n in lista:
        if n not in lista_sin_repetidos:
            lista_sin_repetidos.append(n)

    return lista, lista_sin_repetidos


lista_original, sin_repetidos = quitar_repetidos()
print(f"Lista original: {lista_original}, Lista sin repetidos: {sin_repetidos}")