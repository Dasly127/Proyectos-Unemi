import tkinter as tk
from tkinter import messagebox
from clases import PilaEstudiantes

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")
        self.pila_estudiantes = PilaEstudiantes()
        
        self.create_widgets()

    def create_widgets(self):
        # Crear botones para cada opción del menú
        tk.Button(self.root, text="Agregar estudiante", command=self.agregar_estudiante).pack(pady=5)
        tk.Button(self.root, text="Modificar datos de un estudiante", command=self.modificar_estudiante).pack(pady=5)
        tk.Button(self.root, text="Cambiar estado de un estudiante", command=self.cambiar_estado_estudiante).pack(pady=5)
        tk.Button(self.root, text="Mostrar todos los estudiantes", command=self.mostrar_estudiantes).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def agregar_estudiante(self):
        self.pila_estudiantes.agregar_estudiante()

    def modificar_estudiante(self):
        self.pila_estudiantes.modificar_estudiante()

    def cambiar_estado_estudiante(self):
        self.pila_estudiantes.cambiar_estado_estudiante()

    def mostrar_estudiantes(self):
        estudiantes = self.pila_estudiantes.mostrar_estudiantes()
        messagebox.showinfo("Estudiantes", estudiantes)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
