# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 8: BUCLE FOR — REPETIR X VECES                   ║
# ║  Fase 2: Control de Flujo                               ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Bucle for: repite un número exacto de veces
#    - range(): genera secuencias de números
#    - Recorrer texto letra por letra
#    - Bucles anidados (un for dentro de otro)
#    - Crear patrones y figuras con asteriscos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Modifica los rangos y observa qué cambia
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia07_while.py
# ⏭️ SIGUIENTE: dia09_listas.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: EL BUCLE for
# ============================================================

# for recorre una secuencia de valores.
# En cada repetición, la variable toma el siguiente valor.
#
# for variable in secuencia:
#     código que se repite

# Ejemplo básico:
print("Mis frutas favoritas:")
for fruta in ["manzana", "naranja", "mango", "uva"]:
    print(f"  - {fruta}")

# ============================================================
# SECCIÓN 2: range() — GENERAR SECUENCIAS DE NÚMEROS
# ============================================================

# range(fin)          → números de 0 hasta fin-1
# range(inicio, fin)  → números de inicio hasta fin-1
# range(inicio, fin, paso) → con saltos de "paso"

print("\n--- range(5) ---")
for i in range(5):       # 0, 1, 2, 3, 4
    print(i, end=" ")    # end=" " evita el salto de línea
print()

print("\n--- range(1, 6) ---")
for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

print("\n--- range(0, 20, 2) — pares ---")
for i in range(0, 20, 2):  # 0, 2, 4, 6, ..., 18
    print(i, end=" ")
print()

print("\n--- range(10, 0, -1) — cuenta regresiva ---")
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i, end=" ")
print()

# ============================================================
# SECCIÓN 3: TABLA DE MULTIPLICAR
# ============================================================

numero = int(input("\n¿De qué número quieres la tabla? "))
print(f"\n--- Tabla del {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"  {numero} x {i:2d} = {resultado:3d}")

# ============================================================
# SECCIÓN 4: RECORRER UN STRING (TEXTO)
# ============================================================

# Un for también puede recorrer cada letra de un texto:
palabra = "Python"
print(f"\nLetras de '{palabra}':")
for letra in palabra:
    print(f"  '{letra}'")

# Contar vocales:
frase = "Hola soy Python"
vocales = 0
for letra in frase.lower():
    if letra in "aeiou":
        vocales += 1
print(f"\n'{frase}' tiene {vocales} vocales")

# ============================================================
# SECCIÓN 5: SUMA DEL 1 AL 100
# ============================================================

# Gauss calculó esto de cabeza cuando era niño.
# Python lo hace en microsegundos:

total = 0
for numero in range(1, 101):
    total += numero

print(f"\nSuma de 1 al 100 = {total}")

# Verificación: la fórmula es n*(n+1)/2
print(f"Verificación con fórmula: {100 * 101 // 2}")

# ============================================================
# SECCIÓN 6: BUCLES ANIDADOS — UN FOR DENTRO DE OTRO
# ============================================================

# Cuando tienes un for dentro de otro for, el interno
# se ejecuta COMPLETAMENTE por cada repetición del externo.

print("\n--- Triángulo de asteriscos ---")
for fila in range(1, 6):
    print("*" * fila)  # Imprime 1, luego 2, luego 3... asteriscos

print("\n--- Triángulo invertido ---")
for fila in range(5, 0, -1):
    print("*" * fila)

print("\n--- Tabla de multiplicar 1-5 ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3d}", end="")  # :3d = ancho mínimo de 3 caracteres
    print()  # Salto de línea al final de cada fila

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Números pares del 1 al 50
# ────────────────────────────────────────
# Imprime todos los números pares entre 1 y 50.
# Muéstralos en la misma línea separados por comas.
# Resultado esperado: 2, 4, 6, 8, ..., 50
#
# PISTA: usa range(2, 51, 2) o range(1,51) con if numero % 2 == 0
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Factorial
# ───────────────────────
# El factorial de n es: n! = 1 × 2 × 3 × ... × n
# Por ejemplo: 5! = 1 × 2 × 3 × 4 × 5 = 120
# Pide un número y calcula su factorial.
#
# PISTA: empieza con resultado = 1
#        y dentro del for: resultado = resultado * i
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Rectángulo de asteriscos
# ──────────────────────────────────────
# Pide al usuario ancho y alto.
# Dibuja un rectángulo con asteriscos.
# Ejemplo (ancho=5, alto=3):
# *****
# *****
# *****
#
# Desafío extra: dibuja solo el borde, no el interior:
# *****
# *   *
# *****
#
# ESCRIBE TU CÓDIGO AQUÍ:
