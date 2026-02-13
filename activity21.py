#Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.
def activity21():
    try:


        import math

        x = float(input("Ingrese el Capital Inicial: "))
        y = float(input("Ingrese la Tasa de Interés: ")) / 100
        z = float(input("Ingrese el Número de Períodos: "))

        monto_final = x * math.pow((1 + y), z)

        print("El Monto Final es: ", monto_final)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity21()