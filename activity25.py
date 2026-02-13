#Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.
def activity25():
    try:


        x = int(input("Ingrese el Número de Ventas Realizadas en el Día: "))
        y = float(input("Ingrese el Valor de Cada Venta: "))

        total = x * y
        promedio = total / x

        print("El Total Vendido en el Día es: ", total)
        print("El Promedio por Venta es: ", promedio)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity25()