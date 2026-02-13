#Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).
def activity13():
    try:


        x = float(input("Ingrese la Primera Nota: "))
        y = float(input("Ingrese la Segunda Nota: "))
        z = float(input("Ingrese la Tercera Nota: "))

        promedio = (x + y + z) / 3

        if promedio >= 3.0:
            print("El Estudiante Aprobo con un Promedio de:", promedio)
        elif promedio < 3.0:
            print("El Estudiante Reprobo con un Promedio de:", promedio)
            
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity13()