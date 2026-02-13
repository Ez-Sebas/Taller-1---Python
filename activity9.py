#Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.
def activity9():
    try:
        
        from colorama import init, Fore, Back, Style
        
        init(autoreset=True)
        
        print(Fore.BLUE + "================================================")
        print(Fore.YELLOW + "Venta con IVA")
        print(Fore.BLUE + "================================================")
        
        x = int(input("Ingrese el Valor de la Venta sin Impuestos: "))
        
        iva = x * 0.19
        total = x + iva
            
        print("El Total del Iva es:", iva)
        print("El Total de la Compra es:", int(total))
    
    except ValueError:
        print("Debes Ingresar un Número Válido")
        
if __name__ == "__main__":
    activity9()