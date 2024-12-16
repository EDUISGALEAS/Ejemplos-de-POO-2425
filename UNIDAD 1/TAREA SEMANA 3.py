#PROGRAMACION TRADICIONAL
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para organizar el flujo del programa
def main():
    print("Programa para calcular el promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()

#PROGRAMACION POO

# Definición de la clase Clima
class Clima:
    def __init__(self):
        self.temperaturas = []  # almacenar las temperaturas

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

    # Método para mostrar el promedio semanal
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Función principal POO
def main():
    print("Programa orientado a objetos para calcular el promedio semanal del clima.")
    clima = Clima()  # Crear un objeto de la clase Clima
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    clima.mostrar_promedio()  # Mostrar el promedio semanal

# Llamada a la función principal
if __name__ == "__main__":
    main()

