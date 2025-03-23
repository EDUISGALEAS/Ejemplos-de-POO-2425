import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes agregar una tarea vacía.")

def marcar_completada(event=None):
    try:
        index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(index, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")

# Configuración de la ventana
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

#entrada y botones
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)  # Agregar con Enter

btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)
lista_tareas.bind("<Double-Button-1>", marcar_completada)  # Doble clic para completar

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

root.mainloop()
