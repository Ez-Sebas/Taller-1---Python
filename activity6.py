#Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.
def activity6():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Total de una Venta")
        print(Fore.BLUE + "================================================")
        
        x = input("Ingrese el Nombre del Producto: ")
        y = int(input("Ingrese el Precio Unitario : "))
        z = int(input("Ingrese la Cantidad : "))
        
        total = y * z
        
        print("El Total del Producto es:", int(total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity6()