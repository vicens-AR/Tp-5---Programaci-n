lista = [3,5,6,2]

try:
    indice = int(input("ingrese el numero del indice que desea: "))
    print(f"el numero en su indice es igual a {lista[indice]}")
except IndexError:
    print("Error: El índice está fuera de rango.")