class Libros:
    def __init__(self, titulo, autor, año, codigo):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo

    def __str__(self):
        print(f"Codigo: {self.codigo} Autor: {self.autor} Año: {self.año} Titulo: {self.titulo}")

class Usuarios:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def __str__(self):
        print(f"Carnet: {self.carnet} Nombre: {self.nombre} Carrera: {self.carrera}")

class ManipularLibros:
    def __init__(self):
        self.libros = {}

    def agregar(self):
        try:
            while True:
                try:
                    pass
                except Exception as e:
                    print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

class ManipularUsuarios:
    def __init__(self, usuarios):
        self.usuarios = usuarios


usuarios = {}
libros = {}