try:
    numero1 = int(input("ingrese su primer numero: "))
    numero2 = int(input("ingrese su segundo numero: "))
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)

except ZeroDivisionError:
    print("ERROR: No se puede dividir por zero")

