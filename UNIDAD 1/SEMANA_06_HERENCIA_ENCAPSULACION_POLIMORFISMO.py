#Tarea semana 06

# Definición de Clase (Clase base)
class Vehiculo:
    def __init__(self, marca, modelo, años):
        self._marca = marca  # Atributo protegido (Encapsulación)
        self._modelo = modelo
        self._años = años

    def obtener_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._años}"

    def encender(self):
        return "El vehículo está encendido listo para usar."

# Herencia (Clase derivada)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, años, puertas):
        super().__init__(marca, modelo, años)
        self._puertas = puertas

    # Polimorfismo (Sobrescritura de métodos)
    def obtener_info(self):
        return f"Automóvil -> Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._años}, Puertas: {self._puertas}"

    def encender(self):
        return "El automóvil está encendido listo para usar."

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, años, tipo):
        super().__init__(marca, modelo, años)
        self._tipo = tipo

    def obtener_info(self):
        return f"Motocicleta -> Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._años}, Tipo: {self._tipo}"

    def encender(self):
        return "La motocicleta está encendida lista para usar."

# Definición de Objetos
auto = Automovil("CHEVROLET", "SAIL", 2022, 4)
moto = Motocicleta("SUZUKI", "GN 150", 2021, "Deportiva")

# Uso de Polimorfismo
vehiculos = [auto, moto]

for vehiculo in vehiculos:
    print(vehiculo.obtener_info())
    print(vehiculo.encender())
