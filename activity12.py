#Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.
def activity12():
    try:


        x = int(input("Ingrese el Valor de las Ventas Mensuales: "))

        if x > 1000000:
            comision = x * 0.10
            total = x + comision
        elif x < 1000000:
            comision = x * 0.05
            total = x + comision
            
        print("El Total de la Comisión es:", (total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity12()