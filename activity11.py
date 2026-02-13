#Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
def activity11():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Comisión por Ventas")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese las Ventas Realizadas: "))
        
        comision = x * 0.05
        total = x + comision
        
        print("El Total de la Comisión es: ", int(comision))
        print("El Total a Recibir es: ", int(total))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity11()