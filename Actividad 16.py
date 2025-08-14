class Libros:
    def __init__(self, titulo, autor, año, prestado):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = prestado

    def __str__(self):
        if self.prestado:
            print(f"Autor: {self.autor} Año: {self.año} Titulo: {self.titulo} Prestado: Si")
        else:
            print(f"Autor: {self.autor} Año: {self.año} Titulo: {self.titulo} Prestado: No")

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
                    codigo = int(input("\nCodigo del libro: "))
                    if codigo in self.libros:
                        print("El codigo ya está en uso!!")
                    else:
                        break
                except Exception as e:
                    print(f"Error: {e}")
            while True:
                autor = input("Nombre autor: ")
                if autor or autor.isspace():
                    break
                else:
                    print("Nombre de autor inválido: ")
            while True:
                titulo = input("Título: ")
                if titulo or titulo.isspace():
                    break
                else:
                    print("El título del libro no es válido: ")
            while True:
                try:
                    año = int(input("Ingrese el año de publilcación del libro: "))
                    if año > 0:
                        break
                    else:
                        print("EL año del libro no es válido: ")
                except Exception as e:
                    print(f"Error: {e}")
            prestado = False
            self.libros[codigo] = Libros(titulo, autor, año, prestado)
        except Exception as e:
            print(f"Error: {e}")

class ManipularUsuarios:
    def __init__(self, usuarios):
        self.usuarios = usuarios


usuarios = {}
libros = {}