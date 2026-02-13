#Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.
def activity19():
    try:


        x = float(input("Ingrese el Valor en Pesos Colombianos: "))
        y = float(input("Ingrese la Tasa de Cambio: "))

        dolares = x / y

        print("El Valor en Dólares es: ", dolares)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity19()