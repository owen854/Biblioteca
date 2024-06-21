import tkinter as tk
from tkinter import messagebox
from config import COLOR_CUERPO_PRINCIPAL
from formularios.clases_biblioteca import Libro, Autor, Categoria, biblioteca, Prestamo
from datetime import datetime

class FormularioSitioConstruccionDesign():

    def __init__(self, panel_principal):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Catalogo la Biblioteca")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Botones
        self.boton_registrar = tk.Button(self.barra_inferior, text="Registrar Libros", command=self.mostrar_formulario)
        self.boton_registrar.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=5)

        self.boton_mostrar = tk.Button(self.barra_inferior, text="Mostrar Libros", command=self.mostrar_libros)
        self.boton_mostrar.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=5)

        self.boton_mostrar_prestados = tk.Button(self.barra_inferior, text="Mostrar Libros Prestados", command=self.mostrar_libros_prestados)
        self.boton_mostrar_prestados.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=5)

    def mostrar_formulario(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        tk.Label(self.barra_inferior, text="Registro de Libro", bg=COLOR_CUERPO_PRINCIPAL).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.barra_inferior, text="Título", bg=COLOR_CUERPO_PRINCIPAL).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_titulo = tk.Entry(self.barra_inferior)
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="ISBN", bg=COLOR_CUERPO_PRINCIPAL).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_isbn = tk.Entry(self.barra_inferior)
        self.entry_isbn.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Autor Nombre", bg=COLOR_CUERPO_PRINCIPAL).grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.entry_autor_nombre = tk.Entry(self.barra_inferior)
        self.entry_autor_nombre.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Autor Apellido", bg=COLOR_CUERPO_PRINCIPAL).grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.entry_autor_apellido = tk.Entry(self.barra_inferior)
        self.entry_autor_apellido.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Categoría", bg=COLOR_CUERPO_PRINCIPAL).grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.entry_categoria = tk.Entry(self.barra_inferior)
        self.entry_categoria.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self.barra_inferior, text="Registrar Libro", command=self.registrar_libro).grid(row=6, column=0, columnspan=2, pady=10)

    def registrar_libro(self):
        titulo = self.entry_titulo.get()
        isbn = self.entry_isbn.get()
        autor_nombre = self.entry_autor_nombre.get()
        autor_apellido = self.entry_autor_apellido.get()
        categoria_nombre = self.entry_categoria.get()

        if not (titulo and isbn and autor_nombre and autor_apellido and categoria_nombre):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        autor = Autor(autor_nombre, autor_apellido)
        categoria = Categoria(categoria_nombre)
        libro = Libro(titulo, isbn, autor, categoria)

        biblioteca.libros.append(libro)
        messagebox.showinfo("Registro de Libro", "Libro registrado con éxito")
        self.limpiar_formulario()

    def limpiar_formulario(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_isbn.delete(0, tk.END)
        self.entry_autor_nombre.delete(0, tk.END)
        self.entry_autor_apellido.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)

    def mostrar_libros(self):
        if biblioteca.libros:
            info = "\n".join([libro.mostrar_info() for libro in biblioteca.libros])
        else:
            info = "No hay libros disponibles"
        messagebox.showinfo("Libros Disponibles", info)

    def mostrar_libros_prestados(self):
        libros_prestados = [prestamo for prestamo in biblioteca.prestamos if prestamo.fecha_devolucion is None]
        if libros_prestados:
            info = "\n".join([prestamo.mostrar_info() for prestamo in libros_prestados])
        else:
            info = "No hay libros prestados"
        messagebox.showinfo("Libros Prestados", info)

