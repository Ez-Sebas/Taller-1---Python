#Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.
def activity15():
    try:


        x = int(input("Ingrese un Número: "))
        y = int(input("Ingrese otro Número: "))

        if x > y:
            print("El Número Mayor es:", x)
        elif y > x:
            print("El Número Mayor es:", y)
        else:
            print("Ambos Números son Iguales")
            
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity15()