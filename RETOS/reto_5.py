frase = input("Ingrese una frase: ")
fr = frase.split()

# Imprimir palabras en posiciones pares
for i, palabra in enumerate(fr):
    if i % 2 == 0:
        print(f"[{i}]. {palabra}")

# Imprimir la frase invertida 
frase_invertida = frase[::-1]
print(frase_invertida)

# Dividir la frase en dos mitades 
mitad = len(fr) // 2
primera_mitad = " ".join(fr[:mitad])
segunda_mitad = " ".join(fr[mitad:])

print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

    



    