#Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.
def activity23():
    try:


        x = float(input("Ingrese el Peso del Paquete en Kg: "))

        if x <= 5:
            costo = 10000
            print("El Costo del Envío es: ", costo)
        elif x > 5:
            costo = 20000
            print("El Costo del Envío es: ", costo)
            
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity23() 