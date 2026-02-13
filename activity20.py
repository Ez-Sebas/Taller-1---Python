#Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.
def activity20():
    try:


        x = float(input("Ingrese el Capital: "))
        y = float(input("Ingrese la Tasa de Interés: ")) / 100
        z = float(input("Ingrese el Tiempo en Meses: "))

        interes_simple = x * y * z
        total = x + interes_simple

        print("El Interés Simple es: ", interes_simple)
        print("El Total a Pagar es: ", total)
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity20()