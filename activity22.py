#Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.
def activity22():
    try:


        x = float(input("Ingrese la Cantidad Inicial de un Producto: "))
        y = float(input("Ingrese la Cantidad Vendida: "))
        z = float(input("Ingrese la Cantidad Recibida: "))

        inventario_final = x - y + z

        print("El Total del Inventario Final es: ", inventario_final)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity22()

