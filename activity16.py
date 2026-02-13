#Número par o impar: Solicitar un número entero e indicar si es par o impar.
def activity16():
    try:


        x = float(input("Ingrese un Número: "))

        if x % 2 == 0:
            print("El Número es Par")
        else:
            print("El Número es Impar")
            
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity16()