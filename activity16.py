#Número par o impar: Solicitar un número entero e indicar si es par o impar.
def activity16():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Número Par o Impar")
        print(Fore.BLUE + "================================================")
        
        x = float(input("Ingrese un Número: "))
        
        if x % 2 == 0:
            print("El Número es Par")
        else:
            print("El Número es Impar")
            
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity16()