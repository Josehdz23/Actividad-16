class Libros:
    def __init__(self, titulo, autor, año, prestado):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = prestado

    def mostrar_info(self):
        if self.prestado:
            return f"Autor: {self.autor} | Año: {self.año} | Titulo: {self.titulo} | Prestado: Si"
        else:
            return f"Autor: {self.autor} | Año: {self.año} | Titulo: {self.titulo} | Prestado: No"

class Usuarios:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Carrera: {self.carrera}")

class ManipularLibros:
    def __init__(self):
        self.libros = {}

    def agregar_Libros(self):
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
            prestado = True
            self.libros[codigo] = Libros(titulo, autor, año, prestado)
            print("Libro agregado!!")
        except Exception as e:
            print(f"Error: {e}")

    def mostrar_libros(self):
        if self.libros:
            for codigo, libro in self.libros.items():
                print(f"Codigo: {codigo} | {libro.mostrar_info()}")

class ManipularUsuarios:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def agregar_Usuario(self):
        pass



usuarios = {}
libros = {}

mani = ManipularLibros()
mani.agregar_Libros()
mani.mostrar_libros()
