#Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.
def activity5():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Salario con Horas Extra")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese las Horas Trabajadas: "))
        y = int(input("Ingrese el Valor por hora: "))
        
        if x <= 48:
            salario = x * y
        else:
            z = x - 48
            salario = (48 * y) + (z * y * 1.5)
            
            
        print("El Salario Mensual del Trabajador es:", int(salario))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity5()