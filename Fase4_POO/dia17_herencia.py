# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 17: HERENCIA Y POLIMORFISMO                      ║
# ║  Fase 4: Programación Orientada a Objetos (POO)         ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Herencia: una clase puede "heredar" de otra
#    - super(): llamar al constructor del padre
#    - Polimorfismo: mismo método, diferente comportamiento
#    - Sobreescritura de métodos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Crea subclases nuevas
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia16_clases.py
# ⏭️ SIGUIENTE: dia18_proyecto_inventario.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: HERENCIA
# ============================================================

# La herencia permite que una clase (hija) hereda los atributos
# y métodos de otra clase (padre).
# La clase hija puede agregar nuevos métodos y modificar los heredados.
#
# Analogía: Un PERRO es un ANIMAL. Un GATO es un ANIMAL.
# Ambos tienen cosas en común (nombre, comer, dormir) — eso es el PADRE.
# Pero cada uno tiene cosas propias (ladrar vs maullar) — eso es el HIJO.

# CLASE PADRE (base):
class Animal:
    """Clase base que representa cualquier animal."""

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.energia = 100  # Energía inicial

    def comer(self):
        self.energia += 20
        print(f"🍽️  {self.nombre} está comiendo. Energía: {self.energia}")

    def dormir(self):
        self.energia += 30
        print(f"😴 {self.nombre} está durmiendo. Energía: {self.energia}")

    def info(self):
        print(f"🐾 {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años | Energía: {self.energia}")

    def hacer_sonido(self):
        # Este método será sobreescrito por las subclases
        print(f"{self.nombre} hace un sonido genérico...")


# CLASES HIJAS (heredan de Animal):
class Perro(Animal):
    """Un perro hereda de Animal y agrega comportamientos propios."""

    def __init__(self, nombre, edad, raza):
        # super() llama al __init__ del padre:
        super().__init__(nombre, "Perro", edad)
        self.raza = raza  # Atributo específico de Perro

    # Sobreescritura: reemplazamos el método del padre
    def hacer_sonido(self):
        print(f"🐶 {self.nombre} dice: ¡Guau! ¡Guau!")

    # Método nuevo (no existe en Animal):
    def buscar_pelota(self):
        self.energia -= 10
        print(f"🎾 {self.nombre} busca la pelota. Energía: {self.energia}")

    def info(self):
        super().info()  # Llamamos al info() del padre
        print(f"   Raza: {self.raza}")


class Gato(Animal):
    """Un gato hereda de Animal."""

    def __init__(self, nombre, edad, color):
        super().__init__(nombre, "Gato", edad)
        self.color = color
        self.vidas = 9  # Los gatos tienen 9 vidas 😄

    def hacer_sonido(self):
        print(f"🐱 {self.nombre} dice: ¡Miau!")

    def ronronear(self):
        print(f"😌 {self.nombre} ronronea: prrr... prrr...")

    def info(self):
        super().info()
        print(f"   Color: {self.color} | Vidas restantes: {self.vidas}")


class Pajaro(Animal):
    """Un pájaro hereda de Animal."""

    def __init__(self, nombre, edad, puede_volar=True):
        super().__init__(nombre, "Pájaro", edad)
        self.puede_volar = puede_volar

    def hacer_sonido(self):
        print(f"🐦 {self.nombre} dice: ¡Pío, pío!")

    def volar(self):
        if self.puede_volar:
            self.energia -= 15
            print(f"✈️  {self.nombre} está volando. Energía: {self.energia}")
        else:
            print(f"😢 {self.nombre} no puede volar.")


# ============================================================
# SECCIÓN 2: CREAR INSTANCIAS Y USAR HERENCIA
# ============================================================

fido = Perro("Fido", 3, "Labrador")
whiskers = Gato("Whiskers", 5, "naranja")
tweety = Pajaro("Tweety", 2)
pinguino = Pajaro("Pingo", 4, puede_volar=False)

print("=== Información de los animales ===")
fido.info()
print()
whiskers.info()
print()
tweety.info()
print()

# Polimorfismo: cada animal hace_sonido() de forma diferente
print("=== Todos hacen su sonido ===")
for animal in [fido, whiskers, tweety, pinguino]:
    animal.hacer_sonido()  # Mismo método, diferente resultado

# Métodos heredados (funcionan para todos):
print("\n=== Todos comen ===")
fido.comer()
whiskers.comer()
tweety.comer()

# Métodos específicos:
print("\n=== Métodos específicos ===")
fido.buscar_pelota()
whiskers.ronronear()
tweety.volar()
pinguino.volar()

# ============================================================
# SECCIÓN 3: isinstance() — VERIFICAR TIPO
# ============================================================

print("\n=== Verificar tipos ===")
print(f"¿Fido es un Perro? {isinstance(fido, Perro)}")       # True
print(f"¿Fido es un Animal? {isinstance(fido, Animal)}")     # True (hereda de Animal)
print(f"¿Fido es un Gato? {isinstance(fido, Gato)}")         # False
print(f"¿Whiskers es un Animal? {isinstance(whiskers, Animal)}")  # True

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Vehículo → Coche / Moto / Camión
# ───────────────────────────────────────────────
# Crea una clase Vehiculo con:
#   Atributos: marca, velocidad_max, velocidad_actual (=0), combustible (=100)
#   Métodos: acelerar(), frenar(), repostar(), info()
#
# Crea 3 subclases:
#   - Coche: agrega atributo num_puertas
#   - Moto: agrega atributo tiene_sidecar (bool)
#   - Camion: agrega atributo capacidad_carga (en toneladas)
# Cada subclase sobreescribe info() mostrando sus datos específicos.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Figuras geométricas
# ─────────────────────────────────
# Crea una clase base Figura con:
#   Método: area() → devuelve 0 (será sobreescrito)
#   Método: perimetro() → devuelve 0
#   Método: describir() → imprime "Soy una Figura con área X y perímetro Y"
#
# Crea subclases: Circulo, Rectangulo, Triangulo
# Cada una sobreescribe area() y perimetro() con la fórmula correcta.
#
# ESCRIBE TU CÓDIGO AQUÍ:
