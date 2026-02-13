#Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
def activity3():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Conversión de Temperatura")
        print(Fore.BLUE + "================================================")
        
        c = int(input("Ingrese la Temperatura en celsius: "))
        
        resultado = c * 1.8 + 32
        
        print("La temperatura en Fahrenheir: ", int(resultado))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity3()