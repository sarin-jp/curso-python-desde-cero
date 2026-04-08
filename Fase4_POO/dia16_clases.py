# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 16: CLASES Y OBJETOS                             ║
# ║  Fase 4: Programación Orientada a Objetos (POO)         ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es la Programación Orientada a Objetos (POO)
#    - Cómo crear una clase con class
#    - El método __init__: el constructor
#    - self: referencia al objeto actual
#    - Cómo crear métodos (funciones dentro de clases)
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Crea objetos y llama sus métodos
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: ../Fase3_Funciones/dia15_proyecto_quiz.py
# ⏭️ SIGUIENTE: dia17_herencia.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES LA POO?
# ============================================================

# La Programación Orientada a Objetos modela el mundo real con código.
# En el mundo real, todo son OBJETOS con ATRIBUTOS y COMPORTAMIENTOS.
#
# Ejemplo: Un PERRO tiene:
#   - Atributos: nombre, raza, edad, color
#   - Comportamientos: ladrar, correr, comer
#
# En POO:
#   - Una CLASE es el MOLDE (la plantilla)
#   - Un OBJETO es una INSTANCIA concreta del molde
#
# Analogía:
#   - La clase "Perro" es como el PLANO de una casa
#   - Cada perro concreto (Fido, Rex, Laika) es una INSTANCIA del plano

# ============================================================
# SECCIÓN 2: CREAR UNA CLASE BÁSICA
# ============================================================

class Perro:
    """Clase que representa a un perro."""

    # __init__ es el CONSTRUCTOR: se ejecuta automáticamente al crear un objeto.
    # self es una referencia al objeto que se está creando (obligatorio).
    def __init__(self, nombre, raza, edad):
        # Atributos del objeto (características):
        self.nombre = nombre  # self.nombre guarda el valor EN el objeto
        self.raza = raza
        self.edad = edad
        self.esta_dormido = False  # Atributo con valor por defecto

    # Métodos (comportamientos):
    def ladrar(self):
        if self.esta_dormido:
            print(f"{self.nombre} está dormido... zzz")
        else:
            print(f"{self.nombre} dice: ¡Guau! ¡Guau! 🐶")

    def dormir(self):
        self.esta_dormido = True
        print(f"{self.nombre} se va a dormir 😴")

    def despertar(self):
        self.esta_dormido = False
        print(f"{self.nombre} se despertó 👀")

    def info(self):
        estado = "dormido" if self.esta_dormido else "despierto"
        print(f"🐕 {self.nombre} | Raza: {self.raza} | Edad: {self.edad} años | Estado: {estado}")

    def cumpleaños(self):
        self.edad += 1
        print(f"🎂 ¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")


# ============================================================
# SECCIÓN 3: CREAR OBJETOS (INSTANCIAS)
# ============================================================

# Para crear un objeto, llamamos a la clase como si fuera una función:
fido = Perro("Fido", "Labrador", 3)    # Primera instancia
rex = Perro("Rex", "Pastor Alemán", 5)  # Segunda instancia
laika = Perro("Laika", "Chihuahua", 1) # Tercera instancia

# Cada objeto es independiente:
print("=== Información de los perros ===")
fido.info()
rex.info()
laika.info()

# Llamar métodos:
print("\n=== Interacciones ===")
fido.ladrar()
rex.dormir()
rex.ladrar()   # Rex está dormido
rex.despertar()
rex.ladrar()   # Ahora sí ladra

# Acceder y modificar atributos directamente:
print(f"\nEdad de Laika: {laika.edad}")
laika.cumpleaños()
print(f"Nueva edad: {laika.edad}")

# ============================================================
# SECCIÓN 4: EJEMPLO — CLASE CÍRCULO
# ============================================================

import math

class Circulo:
    """Clase que representa un círculo."""

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def info(self):
        print(f"Círculo con radio {self.radio}")
        print(f"  Área: {self.area():.4f}")
        print(f"  Perímetro: {self.perimetro():.4f}")

    def escalar(self, factor):
        """Multiplica el radio por un factor."""
        self.radio *= factor
        print(f"Nuevo radio: {self.radio}")


c1 = Circulo(5)
c2 = Circulo(10)

print("\n=== Círculos ===")
c1.info()
c2.info()
c1.escalar(2)
c1.info()

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Clase Coche
# ─────────────────────────
# Crea una clase Coche con:
#   Atributos: marca, modelo, año, velocidad (empieza en 0)
#   Métodos:
#     - acelerar(km): aumenta la velocidad
#     - frenar(km): disminuye la velocidad (mínimo 0)
#     - info(): muestra todos los datos
# Crea 2 coches y prueba los métodos.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Clase Rectangulo
# ──────────────────────────────
# Crea una clase Rectangulo con:
#   Atributos: ancho, alto
#   Métodos:
#     - area(): devuelve ancho * alto
#     - perimetro(): devuelve 2 * (ancho + alto)
#     - es_cuadrado(): devuelve True si ancho == alto
#     - info(): muestra todo
# Prueba con diferentes tamaños.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Clase Estudiante
# ──────────────────────────────
# Crea una clase Estudiante con:
#   Atributos: nombre, notas (lista vacía al inicio)
#   Métodos:
#     - agregar_nota(nota): agrega una nota a la lista
#     - promedio(): devuelve el promedio de todas las notas
#     - nota_maxima(): devuelve la nota más alta
#     - aprobo(): devuelve True si el promedio >= 60
#     - informe(): muestra toda la información
#
# ESCRIBE TU CÓDIGO AQUÍ:
