#Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.
def activity4():
    try:
        
        
        x = int(input("Ingrese las Horas Trabajadas: "))
        y = int(input("Ingrese el Valor por hora: "))

        salario = x * y

        print("El Salario Mensual del Trabajador es:", int(salario))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    activity4()