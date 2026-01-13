nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura(mts): "))

print(f"El usuario {nombre}, de {edad} años de edad y mide {altura} metros")

metros = int(altura)
centimetros = int((altura - metros) * 100)

print(f"El usuario {nombre}, de {edad} años de edad y mide {metros} metros y {centimetros} centímetros")