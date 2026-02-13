#Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.
def activity8():
    try:


        x = int(input("Ingrese el Valor del Producto: "))
        y = int(input("Ingrese el Valor del Descuento: "))


        descuento = x * (y / 100)
        total = x - descuento
            
        print("El Total del Descuento es:", int(descuento))
        print("El Total de la Compra es:", int(total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity8()