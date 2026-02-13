import os #Interacua con el sistema operativo (archivos, directorios, rutasm etc)

import sys #Maneja la configuracion y el entorno del interprete de Python          (variables de entorno, argumentos de linea de comandos, etc)

import subprocess #Ejecuta comandos externos y programas, controlando sus entradas/salidas y errores


while True:
    
    from colorama import init, Fore, Back, Style
        
    init(autoreset=True)
    
    print(Fore.BLUE + "================================================")
    print(Fore.YELLOW + "Taller 1 - Algoritmos Basicos en Python")
    print(Fore.YELLOW + "By Sebastian Zuleta Echavarria")   
    print(Fore.YELLOW + "Menu Principal")
    print(Fore.BLUE + "================================================")

    for i in range(1, 26):
        print(f"{i}. Ejecutar Algoritmo {i}")
    print("0. Salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Saliendo ...")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"activity{opcion}.py"

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")

    else:
        print("Opción no válida")     

    input("\n Presiona ENTER para continuar ...")
