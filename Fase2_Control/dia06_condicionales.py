# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 6: CONDICIONALES — if / elif / else               ║
# ║  Fase 2: Control de Flujo                               ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Cómo hacer que tu programa tome decisiones
#    - if, elif, else
#    - Operadores de comparación: ==, !=, >, <, >=, <=
#    - Operadores lógicos: and, or, not
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Cambia los valores y observa el comportamiento
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: ../Fase1_Fundamentos/dia05_proyecto_tarjeta.py
# ⏭️ SIGUIENTE: dia07_while.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ SON LOS CONDICIONALES?
# ============================================================

# Un condicional es una decisión: "SI pasa esto, haz aquello"
# En Python se escribe así:
#
# if condicion:
#     código que se ejecuta si la condición es VERDADERA
# else:
#     código que se ejecuta si la condición es FALSA
#
# MUY IMPORTANTE: El código dentro del if debe tener 4 espacios de sangría
# (VS Code lo hace automáticamente cuando presionas Enter después del :)

edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# ============================================================
# SECCIÓN 2: OPERADORES DE COMPARACIÓN
# ============================================================

# Estos operadores comparan dos valores y devuelven True o False:

a = 10
b = 5

print(f"\n--- COMPARACIONES con a={a}, b={b} ---")
print(f"a == b (son iguales): {a == b}")       # False
print(f"a != b (son distintos): {a != b}")     # True
print(f"a > b  (a es mayor): {a > b}")         # True
print(f"a < b  (a es menor): {a < b}")         # False
print(f"a >= b (mayor o igual): {a >= b}")     # True
print(f"a <= b (menor o igual): {a <= b}")     # False

# Nota: == compara valores, = asigna valores
# print(a = b)  ← ERROR
# print(a == b) ← CORRECTO

# ============================================================
# SECCIÓN 3: elif — MÚLTIPLES CONDICIONES
# ============================================================

# elif = "si no, comprueba si..."
# Puedes tener tantos elif como necesites.

nota = int(input("\nIngresa tu nota (0-100): "))

if nota >= 90:
    print("Calificación: A — ¡Excelente!")
elif nota >= 80:
    print("Calificación: B — ¡Muy bien!")
elif nota >= 70:
    print("Calificación: C — Bien")
elif nota >= 60:
    print("Calificación: D — Aprobado justo")
else:
    print("Calificación: F — Reprobado")

# ============================================================
# SECCIÓN 4: OPERADORES LÓGICOS
# ============================================================

# and → ambas condiciones deben ser True
# or  → al menos una condición debe ser True
# not → invierte True a False y viceversa

print("\n--- OPERADORES LÓGICOS ---")

tiene_licencia = True
es_mayor_de_18 = True
tiene_coche = False

# and: necesita que AMBAS sean True
if tiene_licencia and es_mayor_de_18:
    print("Puedes conducir legalmente ✅")
else:
    print("No puedes conducir ❌")

# or: con que UNA sea True es suficiente
if tiene_licencia or tiene_coche:
    print("Tienes algo relacionado con conducir")
else:
    print("No tienes licencia ni coche")

# not: invierte la condición
if not tiene_coche:
    print("No tienes coche, considera el transporte público")

# Combinando condiciones:
edad_persona = 25
sueldo = 2500

if edad_persona >= 18 and sueldo >= 2000:
    print("\n¡Cumples los requisitos para el préstamo!")
else:
    print("\nNo cumples todos los requisitos para el préstamo.")

# ============================================================
# SECCIÓN 5: EJEMPLO — ¿PUEDES CONDUCIR?
# ============================================================

print("\n" + "="*45)
print("VERIFICADOR DE EDAD PARA CONDUCIR")
print("="*45)

edad_conductor = int(input("¿Cuántos años tienes? "))
tiene_licencia_resp = input("¿Tienes licencia de conducir? (si/no): ").lower()

tiene_lic = tiene_licencia_resp == "si"

if edad_conductor < 16:
    print("❌ Eres demasiado joven para conducir.")
elif edad_conductor < 18:
    if tiene_lic:
        print("⚠️  Puedes conducir con un adulto supervisando.")
    else:
        print("❌ Necesitas licencia y supervisión de adulto.")
elif tiene_lic:
    print("✅ ¡Puedes conducir! Tienes la edad y la licencia.")
else:
    print("⚠️  Tienes la edad pero te falta la licencia.")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Par o impar
# ─────────────────────────
# Pide un número al usuario y di si es par o impar.
# PISTA: un número es par si numero % 2 == 0
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Calculadora con menú
# ───────────────────────────────────
# Pide dos números y una operación (+, -, *, /).
# Muestra el resultado según la operación elegida.
# Si se elige /, verifica que el segundo número no sea 0.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Año bisiesto
# ──────────────────────────
# Un año es bisiesto si:
#   - Es divisible por 4 Y
#   - NO es divisible por 100, O sí es divisible por 400
# Pide un año y di si es bisiesto o no.
# Prueba con: 2024 (bisiesto), 2023 (no), 1900 (no), 2000 (sí)
#
# ESCRIBE TU CÓDIGO AQUÍ:
