import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [producto for producto in self.productos.values() if producto.nombre.lower() == nombre.lower()]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump({id_prod: vars(prod) for id_prod, prod in self.productos.items()}, f, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = {id_prod: Producto(**info) for id_prod, info in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for prod in productos:
                    print(prod)
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
