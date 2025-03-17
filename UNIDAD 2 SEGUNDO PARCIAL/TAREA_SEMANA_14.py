#Tarea semana 14

import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.lista_frame = ttk.Frame(root)
        self.lista_frame.pack(pady=10)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.lista_frame, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack()

        # Frame para la entrada de datos
        self.entrada_frame = ttk.Frame(root)
        self.entrada_frame.pack(pady=10)

        # Labels y Entry para fecha, hora y descripción
        ttk.Label(self.entrada_frame, text='Fecha (YYYY-MM-DD):').grid(row=0, column=0, sticky='w')
        self.fecha_entry = ttk.Entry(self.entrada_frame)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.entrada_frame, text='Hora (HH:MM):').grid(row=1, column=0, sticky='w')
        self.hora_entry = ttk.Entry(self.entrada_frame)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.entrada_frame, text='Descripción:').grid(row=2, column=0, sticky='w')
        self.descripcion_entry = ttk.Entry(self.entrada_frame)
        self.descripcion_entry.grid(row=2, column=1)

        # Frame para los botones
        self.botones_frame = ttk.Frame(root)
        self.botones_frame.pack(pady=10)

        # Botones para agregar, eliminar y salir
        ttk.Button(self.botones_frame, text='Agregar Evento', command=self.agregar_evento).grid(row=0, column=0)
        ttk.Button(self.botones_frame, text='Eliminar Evento', command=self.eliminar_evento).grid(row=0, column=1)
        ttk.Button(self.botones_frame, text='Salir', command=root.destroy).grid(row=0, column=2)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            datetime.datetime.strptime(hora, '%H:%M')
            self.tree.insert('', tk.END, values=(fecha, hora, descripcion))
            self.fecha_entry.delete(0, tk.END)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto. Use YYYY-MM-DD y HH:MM")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el evento seleccionado?")
            if respuesta:
                self.tree.delete(seleccion)
        else:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()