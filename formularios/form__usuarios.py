import tkinter as tk
from tkinter import messagebox
from config import COLOR_CUERPO_PRINCIPAL
from formularios.clases_biblioteca import Usuario, biblioteca

class FormularioUsuarioB():
    def __init__(self, panel_principal):
        self.panel_principal = panel_principal
        
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True) 

        self.labelTitulo = tk.Label(self.barra_superior, text="Usuarios de la Biblioteca")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.mostrar_botones_iniciales()

    def mostrar_botones_iniciales(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        self.boton_registrar = tk.Button(self.barra_inferior, text="Registrar Usuario", command=self.mostrar_formulario_usuario)
        self.boton_registrar.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=10)

        self.boton_mostrar = tk.Button(self.barra_inferior, text="Mostrar Usuarios", command=self.mostrar_usuarios)
        self.boton_mostrar.pack(side=tk.BOTTOM, pady=20, ipadx=10, ipady=10)

    def mostrar_formulario_usuario(self):
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        tk.Label(self.barra_inferior, text="Registro de Usuario", bg=COLOR_CUERPO_PRINCIPAL).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.barra_inferior, text="Nombre", bg=COLOR_CUERPO_PRINCIPAL).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_nombre_usuario = tk.Entry(self.barra_inferior)
        self.entry_nombre_usuario.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="Apellido", bg=COLOR_CUERPO_PRINCIPAL).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_apellido_usuario = tk.Entry(self.barra_inferior)
        self.entry_apellido_usuario.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.barra_inferior, text="DNI", bg=COLOR_CUERPO_PRINCIPAL).grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.entry_dni_usuario = tk.Entry(self.barra_inferior)
        self.entry_dni_usuario.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.barra_inferior, text="Registrar Usuario", command=self.registrar_usuario).grid(row=4, column=0, columnspan=2, pady=10)

    def registrar_usuario(self):
        nombre = self.entry_nombre_usuario.get()
        apellido = self.entry_apellido_usuario.get()
        dni = self.entry_dni_usuario.get()

        if not nombre or not apellido or not dni:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not dni.isdigit():
            messagebox.showerror("Error", "El DNI debe ser un número")
            return

        usuario = Usuario(nombre, apellido, int(dni))
        biblioteca.usuarios.append(usuario)
        messagebox.showinfo("Registro", f"Usuario {nombre} {apellido} registrado correctamente")
        self.mostrar_botones_iniciales()

    def mostrar_usuarios(self):
        usuarios_info = "Lista de Usuarios\n\n"

        for i, usuario in enumerate(biblioteca.usuarios, start=1):
            usuarios_info += f"{i}. {usuario.nombre} {usuario.apellido} - DNI: {usuario.dni}\n"

            for prestamo in usuario.prestamos:
                usuarios_info += f"   {prestamo.mostrar_info()}\n"

        messagebox.showinfo("Lista de Usuarios", usuarios_info)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Formulario de Usuarios")
    panel_principal = tk.Frame(root)
    panel_principal.pack(fill='both', expand=True)
    app = FormularioUsuarioB(panel_principal)
    root.mainloop()
