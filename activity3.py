#Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
def activity3():
    try:


        c = int(input("Ingrese la Temperatura en celsius: "))

        resultado = c * 1.8 + 32

        print("La temperatura en Fahrenheir: ", int(resultado))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity3()