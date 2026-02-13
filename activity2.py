#Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
def activity2():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Área de un Rectángulo")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese la Base del Rectángulo: "))
        y = int(input("Ingrese la Altura del Recángulo: "))
        
        area = x * y
        
        print("La Base del Rectángulo es:", int(area))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity2()