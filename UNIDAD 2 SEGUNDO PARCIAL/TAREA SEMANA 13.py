import tkinter as tk
from tkinter import ttk

def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert("", "end", values=(dato,))
        entrada_texto.delete(0, tk.END)

def limpiar_datos():
    for item in lista_datos.get_children():
        lista_datos.delete(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Crear y ubicar los componentes
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Crear tabla para mostrar los datos
columnas = ("Dato",)
lista_datos = ttk.Treeview(ventana, columns=columnas, show="headings")
lista_datos.heading("Dato", text="Dato")
lista_datos.pack(pady=5, fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
ventana.mainloop()
