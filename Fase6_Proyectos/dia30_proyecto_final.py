# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 30: PROYECTO FINAL — SISTEMA DE BIBLIOTECA       ║
# ║  Fase 6: Proyectos Finales                              ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Integrar TODOS los conceptos del curso
#    - POO: clases Libro y Biblioteca
#    - Persistencia con JSON
#    - Manejo de errores
#    - Menú completo y funcional
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. ¡Es el proyecto final del curso!
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee y entiende todo el código
#    2. Ejecuta el programa y explora el menú
#    3. Agrega libros y prueba todas las funciones
#    4. Añade las mejoras propuestas al final
#
# ⏮️ ANTERIOR: dia29_dashboard.py
# ⏭️ SIGUIENTE: ¡Eres un programador Python! 🎓
# ════════════════════════════════════════════════════════════

import json
import os
import datetime

ARCHIVO_DATOS = "biblioteca.json"

# ============================================================
# CLASE LIBRO
# ============================================================

class Libro:
    """Representa un libro en la biblioteca."""

    def __init__(self, isbn, titulo, autor, año, genero, copias_totales=1):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = int(año)
        self.genero = genero
        self.copias_totales = int(copias_totales)
        self.copias_disponibles = int(copias_totales)
        self.prestamos_historicos = 0
        self.fecha_agregado = datetime.date.today().isoformat()

    @property
    def disponible(self):
        return self.copias_disponibles > 0

    def prestar(self):
        """Registra el préstamo de una copia."""
        if not self.disponible:
            raise ValueError(f"No hay copias disponibles de '{self.titulo}'")
        self.copias_disponibles -= 1
        self.prestamos_historicos += 1

    def devolver(self):
        """Registra la devolución de una copia."""
        if self.copias_disponibles >= self.copias_totales:
            raise ValueError(f"Todas las copias de '{self.titulo}' ya están en biblioteca")
        self.copias_disponibles += 1

    def to_dict(self):
        """Convierte el libro a diccionario para guardar en JSON."""
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "año": self.año,
            "genero": self.genero,
            "copias_totales": self.copias_totales,
            "copias_disponibles": self.copias_disponibles,
            "prestamos_historicos": self.prestamos_historicos,
            "fecha_agregado": self.fecha_agregado
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Libro a partir de un diccionario."""
        libro = cls(
            datos["isbn"],
            datos["titulo"],
            datos["autor"],
            datos["año"],
            datos["genero"],
            datos["copias_totales"]
        )
        libro.copias_disponibles = datos["copias_disponibles"]
        libro.prestamos_historicos = datos.get("prestamos_historicos", 0)
        libro.fecha_agregado = datos.get("fecha_agregado", datetime.date.today().isoformat())
        return libro

    def __str__(self):
        estado = f"✅ {self.copias_disponibles}/{self.copias_totales}" if self.disponible else "❌ No disponible"
        return (f"[{self.isbn}] '{self.titulo}' — {self.autor} "
                f"({self.año}) | {self.genero} | {estado}")


# ============================================================
# CLASE BIBLIOTECA
# ============================================================

class Biblioteca:
    """Sistema de gestión de biblioteca."""

    def __init__(self, nombre, archivo=ARCHIVO_DATOS):
        self.nombre = nombre
        self.archivo = archivo
        self.libros = {}      # isbn → Libro
        self.prestamos = []   # Lista de préstamos activos
        self.cargar_datos()

    def cargar_datos(self):
        """Carga los datos desde el archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    for libro_dict in datos.get("libros", []):
                        libro = Libro.from_dict(libro_dict)
                        self.libros[libro.isbn] = libro
                    self.prestamos = datos.get("prestamos", [])
            except (json.JSONDecodeError, KeyError, IOError):
                print("⚠️  Error cargando datos. Iniciando con biblioteca vacía.")

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON."""
        datos = {
            "nombre": self.nombre,
            "ultima_actualizacion": datetime.datetime.now().isoformat(),
            "libros": [libro.to_dict() for libro in self.libros.values()],
            "prestamos": self.prestamos
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def agregar_libro(self, isbn, titulo, autor, año, genero, copias=1):
        """Agrega un nuevo libro al catálogo."""
        if isbn in self.libros:
            raise ValueError(f"Ya existe un libro con ISBN {isbn}")
        libro = Libro(isbn, titulo, autor, año, genero, copias)
        self.libros[isbn] = libro
        self.guardar_datos()
        print(f"✅ '{titulo}' agregado al catálogo")
        return libro

    def buscar_por_isbn(self, isbn):
        """Busca un libro por ISBN."""
        return self.libros.get(isbn)

    def buscar_por_titulo(self, termino):
        """Busca libros cuyo título contenga el término."""
        termino = termino.lower()
        return [l for l in self.libros.values() if termino in l.titulo.lower()]

    def buscar_por_autor(self, autor):
        """Busca libros de un autor específico."""
        autor = autor.lower()
        return [l for l in self.libros.values() if autor in l.autor.lower()]

    def buscar_por_genero(self, genero):
        """Busca libros de un género específico."""
        genero = genero.lower()
        return [l for l in self.libros.values() if genero in l.genero.lower()]

    def prestar_libro(self, isbn, nombre_usuario):
        """Registra el préstamo de un libro."""
        libro = self.buscar_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No existe libro con ISBN {isbn}")

        libro.prestar()

        prestamo = {
            "id": len(self.prestamos) + 1,
            "isbn": isbn,
            "titulo": libro.titulo,
            "usuario": nombre_usuario,
            "fecha_prestamo": datetime.date.today().isoformat(),
            "fecha_devolucion_esperada": (datetime.date.today() + datetime.timedelta(days=14)).isoformat(),
            "devuelto": False
        }
        self.prestamos.append(prestamo)
        self.guardar_datos()
        print(f"✅ '{libro.titulo}' prestado a {nombre_usuario}")
        print(f"   Fecha de devolución: {prestamo['fecha_devolucion_esperada']}")
        return prestamo

    def devolver_libro(self, isbn, nombre_usuario):
        """Registra la devolución de un libro."""
        libro = self.buscar_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No existe libro con ISBN {isbn}")

        # Buscar préstamo activo:
        prestamo_encontrado = None
        for p in self.prestamos:
            if p["isbn"] == isbn and p["usuario"] == nombre_usuario and not p["devuelto"]:
                prestamo_encontrado = p
                break

        if not prestamo_encontrado:
            raise ValueError(f"No hay préstamo activo de '{isbn}' para {nombre_usuario}")

        libro.devolver()
        prestamo_encontrado["devuelto"] = True
        prestamo_encontrado["fecha_devolucion_real"] = datetime.date.today().isoformat()
        self.guardar_datos()
        print(f"✅ '{libro.titulo}' devuelto por {nombre_usuario}")

    def mostrar_catalogo(self, solo_disponibles=False):
        """Muestra el catálogo de libros."""
        libros_mostrar = self.libros.values()
        if solo_disponibles:
            libros_mostrar = [l for l in libros_mostrar if l.disponible]

        if not libros_mostrar:
            print("📚 No hay libros" + (" disponibles" if solo_disponibles else ""))
            return

        titulo = "CATÁLOGO COMPLETO" if not solo_disponibles else "LIBROS DISPONIBLES"
        print(f"\n{'='*65}")
        print(f"  📚 {self.nombre} — {titulo} ({len(list(libros_mostrar))} libros)")
        print(f"{'='*65}")
        for libro in sorted(libros_mostrar, key=lambda l: l.titulo):
            print(f"  {libro}")
        print(f"{'='*65}")

    def estadisticas(self):
        """Muestra estadísticas de la biblioteca."""
        total = len(self.libros)
        disponibles = sum(1 for l in self.libros.values() if l.disponible)
        prestados = sum(1 for p in self.prestamos if not p["devuelto"])
        total_prestamos = len(self.prestamos)

        generos = {}
        for l in self.libros.values():
            generos[l.genero] = generos.get(l.genero, 0) + 1

        mas_prestado = max(self.libros.values(),
                           key=lambda l: l.prestamos_historicos,
                           default=None)

        print(f"\n{'='*55}")
        print(f"  📊 ESTADÍSTICAS — {self.nombre}")
        print(f"{'='*55}")
        print(f"  Total de libros:      {total:>5}")
        print(f"  Disponibles:          {disponibles:>5}")
        print(f"  Préstamos activos:    {prestados:>5}")
        print(f"  Préstamos históricos: {total_prestamos:>5}")

        if generos:
            print(f"\n  Libros por género:")
            for genero, cantidad in sorted(generos.items(), key=lambda x: x[1], reverse=True):
                barra = "█" * cantidad
                print(f"    {genero:<20} {barra} ({cantidad})")

        if mas_prestado and mas_prestado.prestamos_historicos > 0:
            print(f"\n  📖 Libro más popular: '{mas_prestado.titulo}'")
            print(f"     ({mas_prestado.prestamos_historicos} préstamos)")
        print(f"{'='*55}")


# ============================================================
# DATOS DE EJEMPLO
# ============================================================

def cargar_datos_ejemplo(biblioteca):
    """Carga libros de ejemplo si la biblioteca está vacía."""
    if biblioteca.libros:
        return

    libros_ejemplo = [
        ("978-0-06-112008-4", "Matar un ruiseñor", "Harper Lee", 1960, "Ficción", 3),
        ("978-0-7432-7356-5", "El gran Gatsby", "F. Scott Fitzgerald", 1925, "Ficción", 2),
        ("978-0-14-028329-7", "1984", "George Orwell", 1949, "Distopía", 4),
        ("978-0-7432-7357-2", "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo Mágico", 2),
        ("978-0-06-093546-9", "El principito", "Antoine de Saint-Exupéry", 1943, "Fábula", 5),
        ("978-84-204-8223-3", "El nombre de la rosa", "Umberto Eco", 1980, "Misterio", 2),
        ("978-0-679-72020-1", "Don Quijote", "Miguel de Cervantes", 1605, "Aventura", 3),
        ("978-0-7432-7001-4", "Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía", 4),
    ]

    print("📚 Cargando biblioteca con libros de ejemplo...")
    for isbn, titulo, autor, año, genero, copias in libros_ejemplo:
        try:
            biblioteca.agregar_libro(isbn, titulo, autor, año, genero, copias)
        except ValueError:
            pass


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu(biblioteca):
    """Menú interactivo del sistema."""
    print("\n" + "╔" + "═"*50 + "╗")
    print("║" + f"  📚 {biblioteca.nombre}  ".center(50) + "║")
    print("║" + f"  {len(biblioteca.libros)} libros en catálogo  ".center(50) + "║")
    print("╚" + "═"*50 + "╝")
    print("  1. Ver catálogo completo")
    print("  2. Ver libros disponibles")
    print("  3. Buscar libro")
    print("  4. Agregar libro")
    print("  5. Prestar libro")
    print("  6. Devolver libro")
    print("  7. Ver estadísticas")
    print("  0. Salir")


def main():
    biblioteca = Biblioteca("Biblioteca Python")
    cargar_datos_ejemplo(biblioteca)

    print("\n" + "═"*55)
    print(f"  Bienvenido a {biblioteca.nombre}")
    print("═"*55)

    while True:
        menu(biblioteca)
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            biblioteca.mostrar_catalogo()

        elif opcion == "2":
            biblioteca.mostrar_catalogo(solo_disponibles=True)

        elif opcion == "3":
            print("\nBuscar por:")
            print("  1. Título")
            print("  2. Autor")
            print("  3. Género")
            print("  4. ISBN")
            sub = input("Tipo de búsqueda: ")

            if sub == "1":
                termino = input("Título (o parte del título): ")
                resultados = biblioteca.buscar_por_titulo(termino)
            elif sub == "2":
                termino = input("Nombre del autor: ")
                resultados = biblioteca.buscar_por_autor(termino)
            elif sub == "3":
                termino = input("Género: ")
                resultados = biblioteca.buscar_por_genero(termino)
            elif sub == "4":
                isbn = input("ISBN: ")
                libro = biblioteca.buscar_por_isbn(isbn)
                resultados = [libro] if libro else []
            else:
                print("❌ Opción no válida")
                continue

            if resultados:
                print(f"\n{len(resultados)} resultado(s):")
                for l in resultados:
                    print(f"  {l}")
            else:
                print("❌ No se encontraron libros")

        elif opcion == "4":
            print("\n── Agregar nuevo libro ──")
            try:
                isbn = input("ISBN: ").strip()
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                año = input("Año de publicación: ").strip()
                genero = input("Género: ").strip()
                copias = int(input("Número de copias [1]: ").strip() or "1")
                biblioteca.agregar_libro(isbn, titulo, autor, int(año), genero, copias)
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "5":
            biblioteca.mostrar_catalogo(solo_disponibles=True)
            isbn = input("\nISBN del libro a prestar: ").strip()
            usuario = input("Nombre del usuario: ").strip()
            try:
                biblioteca.prestar_libro(isbn, usuario)
            except ValueError as e:
                print(f"❌ {e}")

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ").strip()
            usuario = input("Nombre del usuario: ").strip()
            try:
                biblioteca.devolver_libro(isbn, usuario)
            except ValueError as e:
                print(f"❌ {e}")

        elif opcion == "7":
            biblioteca.estadisticas()

        elif opcion == "0":
            print("\n" + "╔" + "═"*56 + "╗")
            print("║" + "  ".center(56) + "║")
            print("║" + "  🎓 ¡FELICIDADES! ¡COMPLETASTE EL CURSO!  ".center(56) + "║")
            print("║" + "  ".center(56) + "║")
            print("║" + "  Has completado los 30 días de Python.  ".center(56) + "║")
            print("║" + "  ".center(56) + "║")
            print("║" + "  Lo que aprendiste:  ".center(56) + "║")
            print("║" + "  ✅ Fase 1: Fundamentos — print, variables, strings  ".center(56) + "║")
            print("║" + "  ✅ Fase 2: Control — if, while, for, listas  ".center(56) + "║")
            print("║" + "  ✅ Fase 3: Funciones — def, lambda, módulos  ".center(56) + "║")
            print("║" + "  ✅ Fase 4: POO — clases, herencia, encapsulamiento  ".center(56) + "║")
            print("║" + "  ✅ Fase 5: Archivos — CSV, JSON, APIs, SQLite  ".center(56) + "║")
            print("║" + "  ✅ Fase 6: Proyectos reales y completos  ".center(56) + "║")
            print("║" + "  ".center(56) + "║")
            print("║" + "  ¿Qué sigue?  ".center(56) + "║")
            print("║" + "  🌐 Django/Flask — crea sitios web con Python  ".center(56) + "║")
            print("║" + "  📊 Pandas/NumPy — análisis de datos  ".center(56) + "║")
            print("║" + "  🤖 TensorFlow/sklearn — inteligencia artificial  ".center(56) + "║")
            print("║" + "  🔧 FastAPI — crea APIs REST profesionales  ".center(56) + "║")
            print("║" + "  ".center(56) + "║")
            print("║" + "  ¡El cielo es el límite, programador! 🐍🚀  ".center(56) + "║")
            print("║" + "  ".center(56) + "║")
            print("╚" + "═"*56 + "╝")
            break

        else:
            print("❌ Opción no válida")

    # Limpiar archivo al terminar:
    if os.path.exists(ARCHIVO_DATOS):
        os.remove(ARCHIVO_DATOS)


main()
