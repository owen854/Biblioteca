import datetime

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria
        self.prestado = False

    def mostrar_info(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro: {self.titulo}\nISBN: {self.isbn}\nAutor: {self.autor.nombre} {self.autor.apellido}\nCategoría: {self.categoria.nombre}\nEstado: {estado}\n"

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self): 
        return f"Autor: {self.nombre} {self.apellido}"

class Usuario:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.prestamos = []

    def mostrar_info(self):
        info = f"Usuario: {self.nombre} {self.apellido}\nDNI: {self.dni}\nPréstamos:\n"
        for prestamo in self.prestamos:
            info += prestamo.mostrar_info() + "\n"
        return info

# class Usuario:
#     def __init__(self, nombre, apellido, dni):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.dni = dni
#         self.prestamos = []


# 7class Usuario:
#     def __init__(self, nombre, apellido, id_usuario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.id_usuario = id_usuario
#         self.prestamos = []

    # def mostrar_info(self):
    #     info = f"Usuario: {self.nombre} {self.apellido}\nID de usuario: {self.id_usuario}\nPréstamos:\n"
    #     for prestamo in self.prestamos:
    #         info += prestamo.mostrar_info() + "\n"
    #     return info

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        info = f"Préstamo:\nLibro: {self.libro.titulo}\nUsuario: {self.usuario.nombre} {self.usuario.apellido}\nFecha de préstamo: {self.fecha_prestamo}\n"
        if self.fecha_devolucion:
            info += f"Fecha de devolución: {self.fecha_devolucion}\n"
        else:
            info += "Libro aún no devuelto\n"
        return info

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, usuario, libro):
        if libro.prestado:
            return f"El libro '{libro.titulo}' ya ha sido prestado"
        prestamo = Prestamo(libro, usuario, datetime.datetime.now())
        usuario.prestamos.append(prestamo)
        self.prestamos.append(prestamo)
        libro.prestado = True
        return f"Préstamo realizado para {usuario.nombre} {usuario.apellido} con el libro {libro.titulo}"

    def devolver_libro(self, prestamo):
        prestamo.fecha_devolucion = datetime.datetime.now()
        prestamo.libro.prestado = False
        return f"Libro {prestamo.libro.titulo} devuelto por {prestamo.usuario.nombre} {prestamo.usuario.apellido}"

    def mostrar_libros(self):
        info = "Libros disponibles:\n"
        for libro in self.libros:
            info += libro.mostrar_info() + "\n"
        return info

    def mostrar_usuarios(self):
        info = "Usuarios registrados:\n"
        for usuario in self.usuarios:
            info += usuario.mostrar_info() + "\n"
        return info

    def mostrar_libros_prestados(self):
        info = "Libros Prestados:\n"
        for prestamo in self.prestamos:
            if not prestamo.fecha_devolucion:
                info += prestamo.mostrar_info() + "\n"
        return info
    
biblioteca = Biblioteca()