#Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.
def activity7():
    try:


        x = int(input("Ingrese el Valor Total de la Compra: "))

        if x > 200000:
            descuento = x * 0.10
            total = x - descuento
        elif x < 200000:
            total = x 
            
            
        print("El Total de la Compra es:", int(total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity7()