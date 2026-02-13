#Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.
def activity18():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Clasificación por Edad")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese su Edad: "))
        
        if x >= 18 and x < 60:
            print("Eres Mayor de Edad")
        elif x >= 60 and x < 100:
            print("Eres un Adulto Mayor")
        else :
            print("Eres Menor de Edad")
            
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity18()