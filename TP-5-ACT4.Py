try:
    numero1 = int(input("ingrese su primer numero: "))
    numero2 = int(input("ingrese su segundo numero: "))
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"la suma es igual a: {suma} y la resta es igual a: {resta}")

except TypeError:
    print("ERROR: No es el tipo de dato esperado ")