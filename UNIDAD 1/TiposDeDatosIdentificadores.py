#Este program se realiza para calcular el area de figuras un circulo,
# rectangulo, triangulo donde vamos a verificar el dato que requiera el usuario
#lo llamatitvo de este codigo es q permite al usurio seguir dentro del programa
# hasta que el decida si continuar ingresa el dato "si" y si quiere salir presiona "no"
#en el programa se ha utizado las directrices emitidas.


def mostrar_menu():
    """
    Mostrar el menú al usuario.
    """
    print("CÁLCULO DE ÁREA ")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Salir")


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return 3.1416 * radio ** 2


def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dada su base y altura.
    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return base * altura


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.
    :param base: Base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    return (base * altura) / 2


def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")

        elif opcion == "2":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area:.2f}")

        elif opcion == "3":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")

        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Inténtalo nuevamente.")

        # Preguntar si desea continuar
        continuar = input("¿Quieres realizar otro cálculo? (sí/no): ").strip().lower()
        if continuar != "sí":
            print("¡Adiós!")
            break


if __name__ == "__main__":
    main()
