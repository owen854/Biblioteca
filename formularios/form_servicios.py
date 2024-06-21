from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from config import COLOR_CUERPO_PRINCIPAL
from formularios.clases_biblioteca import Libro, Autor, Categoria, Prestamo, Usuario, biblioteca, Biblioteca

class FormularioServiciosB():
    def __init__(self, panel_principal):
        self.panel_principal = panel_principal

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.labelTitulo = tk.Label(self.barra_superior, text="Servicios de la Biblioteca")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.mostrar_botones_iniciales()

    def mostrar_botones_iniciales(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        self.boton_prestamo = tk.Button(self.barra_inferior, text="Realizar Préstamo", command=self.mostrar_formulario_prestamo)
        self.boton_prestamo.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=10)

        self.boton_devolucion = tk.Button(self.barra_inferior, text="Devolver Libro", command=self.mostrar_formulario_devolucion)
        self.boton_devolucion.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=10)

    def mostrar_formulario_prestamo(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        tk.Label(self.barra_inferior, text="Realizar Préstamo", bg=COLOR_CUERPO_PRINCIPAL).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.barra_inferior, text="ID Usuario", bg=COLOR_CUERPO_PRINCIPAL).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_dni_prestamo_usuario = tk.Entry(self.barra_inferior)
        self.entry_dni_prestamo_usuario.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Nombre Libro", bg=COLOR_CUERPO_PRINCIPAL).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_nombre_libro = tk.Entry(self.barra_inferior)
        self.entry_nombre_libro.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.barra_inferior, text="Realizar Préstamo", command=self.realizar_prestamo).grid(row=3, column=0, columnspan=2, pady=10)

    def mostrar_formulario_devolucion(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        tk.Label(self.barra_inferior, text="Devolver Libro", bg=COLOR_CUERPO_PRINCIPAL).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.barra_inferior, text="ID Usuario", bg=COLOR_CUERPO_PRINCIPAL).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_dni_prestamo_usuario = tk.Entry(self.barra_inferior)
        self.entry_dni_prestamo_usuario.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Nombre Libro", bg=COLOR_CUERPO_PRINCIPAL).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_nombre_libro = tk.Entry(self.barra_inferior)
        self.entry_nombre_libro.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.barra_inferior, text="Devolver Libro", command=self.devolver_libro).grid(row=3, column=0, columnspan=2, pady=10)

    def realizar_prestamo(self):
        dni = self.entry_dni_prestamo_usuario.get()
        titulo_libro = self.entry_nombre_libro.get()

        if not dni:
            messagebox.showerror("Error", "ID de Usuario no puede estar vacío")
            return

        try:
            dni = int(dni)
        except ValueError:
            messagebox.showerror("Error", "ID de Usuario debe ser un número entero")
            return

        usuario = next((u for u in biblioteca.usuarios if u.dni == dni), None)
        libro = next((l for l in biblioteca.libros if l.titulo == titulo_libro), None)

        if usuario and libro:
            resultado = biblioteca.realizar_prestamo(usuario, libro)
            messagebox.showinfo("Préstamo", resultado)
            self.mostrar_botones_iniciales()
        elif not usuario:
            messagebox.showerror("Error", "Usuario no encontrado")
        elif not libro:
            messagebox.showerror("Error", "Libro no encontrado")

    def devolver_libro(self):
        dni = self.entry_dni_prestamo_usuario.get()
        titulo_libro = self.entry_nombre_libro.get()

        if not dni:
            messagebox.showerror("Error", "ID de Usuario no puede estar vacío")
            return

        try:
            dni = int(dni)
        except ValueError:
            messagebox.showerror("Error", "ID de Usuario debe ser un número entero")
            return

        usuario = next((u for u in biblioteca.usuarios if u.dni == dni), None)

        if usuario:
            prestamo = next((p for p in usuario.prestamos if p.libro.titulo == titulo_libro), None)
            if prestamo:
                resultado = biblioteca.devolver_libro(prestamo)
                messagebox.showinfo("Devolución", resultado)
                self.mostrar_botones_iniciales()
            else:
                messagebox.showerror("Error", "Préstamo no encontrado")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")
