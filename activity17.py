#Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.
def activity17():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Edad de una Persona")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese el Año de Nacimiento: "))
        y = int(input("Ingrese el Año Actual: "))
        
        edad = y - x 
        
        print("Tu Edad es: ", edad)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity17()
