import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack()

        self.add_button = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(frame_buttons, text="Completar Tarea", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.listbox.pack(pady=10)

        # Manejadores de teclas
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para completar.")

    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["text"]
            if task["completed"]:
                display_text = f"✔ {display_text}"
            self.listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.listbox.itemconfig(tk.END, {'fg': 'gray'})

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
