#Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.
def activity24():
    try:


        x = float(input("Ingres el Consumo de Agua en Metros Cúbico: "))
        y = float(input("Ingres el Valor por Metro Cúbico: "))

        valor_total = x * y

        print("El Valor Total de la Factura es: ", int(valor_total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity24()