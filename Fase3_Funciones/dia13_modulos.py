# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 13: MÓDULOS — SUPERPODERES DE PYTHON             ║
# ║  Fase 3: Funciones                                      ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es un módulo y cómo importarlo
#    - math: funciones matemáticas avanzadas
#    - random: números aleatorios
#    - datetime: fechas y horas
#    - string: constantes de caracteres
#    - PROYECTO: Generador de contraseñas seguras
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con los módulos
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia12_funciones_avanzadas.py
# ⏭️ SIGUIENTE: dia14_errores.py
# ════════════════════════════════════════════════════════════

# Los módulos son colecciones de funciones ya escritas por otros.
# No tienes que reinventar la rueda: ¡úsalos!
# Para usar un módulo: import nombre_modulo

import math      # Funciones matemáticas
import random    # Números aleatorios
import datetime  # Fechas y horas
import string    # Constantes de texto (letras, dígitos, etc.)

# ============================================================
# SECCIÓN 1: MÓDULO math
# ============================================================

print("=" * 45)
print("MÓDULO math — Matemáticas avanzadas")
print("=" * 45)

# Constantes:
print(f"\nPi (π): {math.pi}")
print(f"Número de Euler (e): {math.e:.6f}")

# Funciones de redondeo:
print(f"\nmath.ceil(4.1) = {math.ceil(4.1)}")    # Redondea hacia arriba: 5
print(f"math.floor(4.9) = {math.floor(4.9)}")   # Redondea hacia abajo: 4
print(f"math.trunc(4.9) = {math.trunc(4.9)}")   # Trunca (quita decimales): 4
print(f"round(4.567, 2) = {round(4.567, 2)}")   # Redondea a 2 decimales: 4.57

# Funciones matemáticas:
print(f"\nRaíz cuadrada de 144: {math.sqrt(144)}")        # 12.0
print(f"Valor absoluto de -15: {math.fabs(-15)}")         # 15.0
print(f"2^10 = {math.pow(2, 10)}")                        # 1024.0
print(f"Logaritmo natural de e: {math.log(math.e):.4f}") # 1.0

# Trigonometría (en radianes):
angulo_grados = 45
angulo_radianes = math.radians(angulo_grados)
print(f"\nSeno de 45° = {math.sin(angulo_radianes):.4f}")   # 0.7071
print(f"Coseno de 60° = {math.cos(math.radians(60)):.4f}") # 0.5

# Ejemplo: área de un círculo con math.pi
def area_circulo(radio):
    return math.pi * radio ** 2

print(f"\nÁrea de un círculo con radio 5: {area_circulo(5):.2f}")

# ============================================================
# SECCIÓN 2: MÓDULO random
# ============================================================

print("\n" + "=" * 45)
print("MÓDULO random — Números aleatorios")
print("=" * 45)

# random.randint(a, b) → entero aleatorio entre a y b (inclusivo)
print(f"\nNúmero aleatorio entre 1 y 100: {random.randint(1, 100)}")
print(f"Número aleatorio entre 1 y 6 (dado): {random.randint(1, 6)}")

# random.random() → decimal aleatorio entre 0 y 1
print(f"\nDecimal aleatorio: {random.random():.4f}")

# random.choice(lista) → elige un elemento aleatorio
frutas = ["manzana", "naranja", "mango", "uva", "pera"]
print(f"\nFruta aleatoria: {random.choice(frutas)}")

colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Color aleatorio: {random.choice(colores)}")

# random.sample(lista, k) → elige k elementos sin repetir
print(f"\n3 frutas aleatorias sin repetir: {random.sample(frutas, 3)}")

# random.shuffle(lista) → mezcla una lista (la modifica en lugar)
cartas = ["A", "2", "3", "4", "5", "J", "Q", "K"]
random.shuffle(cartas)
print(f"Baraja mezclada: {cartas}")

# ============================================================
# SECCIÓN 3: MÓDULO datetime
# ============================================================

print("\n" + "=" * 45)
print("MÓDULO datetime — Fechas y horas")
print("=" * 45)

# Fecha y hora actual:
ahora = datetime.datetime.now()
print(f"\nFecha y hora actual: {ahora}")
print(f"Solo la fecha: {ahora.date()}")
print(f"Solo la hora: {ahora.time()}")
print(f"Año: {ahora.year}")
print(f"Mes: {ahora.month}")
print(f"Día: {ahora.day}")

# Formatear fechas (strftime = "string format time"):
print(f"\nFormato bonito: {ahora.strftime('%d/%m/%Y %H:%M')}")
print(f"Solo día y mes: {ahora.strftime('%d de %B')}")

# Crear una fecha específica:
fecha_inicio = datetime.date(2024, 1, 1)
fecha_hoy = datetime.date.today()
diferencia = fecha_hoy - fecha_inicio
print(f"\nDías desde el 1 de enero 2024: {diferencia.days}")

# ============================================================
# SECCIÓN 4: MÓDULO string
# ============================================================

print("\n" + "=" * 45)
print("MÓDULO string — Constantes de texto")
print("=" * 45)

print(f"Letras minúsculas: {string.ascii_lowercase}")
print(f"Letras mayúsculas: {string.ascii_uppercase}")
print(f"Todas las letras: {string.ascii_letters}")
print(f"Dígitos: {string.digits}")
print(f"Puntuación: {string.punctuation}")

# ============================================================
# SECCIÓN 5: PROYECTO — GENERADOR DE CONTRASEÑAS
# ============================================================

print("\n" + "="*50)
print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS")
print("="*50)

def generar_contrasena(longitud=12, usar_mayusculas=True,
                       usar_numeros=True, usar_simbolos=True):
    """Genera una contraseña aleatoria y segura."""

    # Construir el conjunto de caracteres disponibles
    caracteres = string.ascii_lowercase  # Siempre incluye minúsculas

    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%^&*"

    # Generar la contraseña
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def evaluar_seguridad(contrasena):
    """Evalúa la seguridad de una contraseña."""
    puntos = 0
    if len(contrasena) >= 8:
        puntos += 1
    if len(contrasena) >= 12:
        puntos += 1
    if any(c.isupper() for c in contrasena):
        puntos += 1
    if any(c.isdigit() for c in contrasena):
        puntos += 1
    if any(c in "!@#$%^&*" for c in contrasena):
        puntos += 1

    if puntos <= 2:
        return "❌ Débil"
    elif puntos <= 3:
        return "⚠️  Media"
    elif puntos == 4:
        return "✅ Fuerte"
    else:
        return "🔒 Muy fuerte"

# Generar varias contraseñas:
print("\n📋 Contraseñas generadas:")
for i in range(5):
    pwd = generar_contrasena(longitud=16)
    seguridad = evaluar_seguridad(pwd)
    print(f"  {i+1}. {pwd}  →  {seguridad}")

# Menú interactivo:
print("\n¿Quieres personalizar tu contraseña?")
longitud = int(input("Longitud (8-32): "))
longitud = max(8, min(32, longitud))  # Clamp entre 8 y 32

mi_pwd = generar_contrasena(longitud)
print(f"\n🔑 Tu contraseña: {mi_pwd}")
print(f"   Seguridad: {evaluar_seguridad(mi_pwd)}")
print(f"   Longitud: {len(mi_pwd)} caracteres")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Cálculos con math
# ───────────────────────────────
# Calcula y muestra:
# - El área de un círculo con radio pedido al usuario (π × r²)
# - La hipotenusa de un triángulo rectángulo (√(a² + b²))
# - Redondear un número decimal hacia arriba y hacia abajo
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Números aleatorios ordenados
# ──────────────────────────────────────────
# Genera 10 números aleatorios entre 1 y 100.
# Muéstralos en el orden en que se generaron.
# Luego muéstralos ordenados de menor a mayor.
# Muestra también el mayor y el menor.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Fecha formateada
# ──────────────────────────────
# Muestra la fecha de hoy en el formato: "Hoy es lunes, 15 de marzo de 2024"
# Calcula cuántos días faltan para el 31 de diciembre del año actual.
# PISTA: usa datetime.date.today() y datetime.date(año, 12, 31)
#
# ESCRIBE TU CÓDIGO AQUÍ:
