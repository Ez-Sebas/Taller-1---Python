#Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.
def activity10():
    try:


        x = int(input("Ingrese el Valor Total de los Productos: "))
        y = int(input("Ingrese el Precio de Cada uno: "))

        total = x * y

        print("El Total de la Compra es:", int(total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity10()