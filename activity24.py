#Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.
def activity24():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Factura de Servicios Públicos")
        print(Fore.BLUE + "================================================")
        
        x = float(input("Ingrese el Consumo de Agua en Metros Cúbico: "))
        y = float(input("Ingrese el Valor por Metro Cúbico: "))
        
        valor_total = x * y
        
        print("El Valor Total de la Factura es: ", int(valor_total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity24()