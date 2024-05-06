try:
    numero = int(input("ingrese su primer numero: "))
    print(f"Tu numero es {numero}")

except ValueError:
    print("ERROR: Ingrese un numero valido")