#Entrada
def activity1():
    try:


        x = int(input("Ingrese el Número Entero: "))
        y = int(input("Ingrese el Número Entero: "))
        z = int(input("Ingrese el Número Entero: "))

        #Procedimiento
        suma = x + y + z
        average = suma / 3

        #Salidas
        print("La Suma Total es:", suma)
        print("El Promedio es:", int(average))

    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity1()