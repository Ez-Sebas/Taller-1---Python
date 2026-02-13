#Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.
def activity14():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Nota Final Ponderada")
        print(Fore.BLUE + "================================================")
        
        x = float(input("Ingrese la Nota del Taller: "))
        y = float(input("Ingrese la Nota del Examen Parcial: "))
        z = float(input("Ingrese la Nota del Examen Final: "))
        
        nota = (x * 0.30) + (y * 0.30) + (z * 0.40)
        
        print("La Nota Definitiva de Estudiante es: ", nota)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity14()