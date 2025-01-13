#ejemplos del mundo real

class Ave:
    def volar(self):
        print("El pajaro vuela.")
class Pinguino(Ave):
    def volar(self):
        print("El perro no vuela.")

#EJEMPLO DE AUTO
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
mi_coche = Coche("NISSAN", "TIHIDA")

#EJEMPLO DE CUENTA BANCARIA
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado
    def depositar(self, monto):
        self.__saldo += monto
    def obtener_saldo(self):
        return self.__saldo
