# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 3: ENTRADA DEL USUARIO Y OPERADORES              ║
# ║  Fase 1: Fundamentos                                    ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Cómo pedir información al usuario con input()
#    - Cómo convertir texto a número con int() y float()
#    - Todos los operadores aritméticos: +, -, *, /, //, %, **
#    - Cómo hacer una calculadora simple
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Cuando aparezca "¿Cómo te llamas?", ESCRIBE tu nombre y presiona Enter
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa y responde las preguntas
#    3. Modifica las preguntas y experimenta
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia02_variables.py
# ⏭️ SIGUIENTE: dia04_strings.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: LA FUNCIÓN input()
# ============================================================

# input() pausa el programa y espera que el usuario escriba algo.
# Lo que el usuario escribe se guarda como texto (str).

# Sintaxis: variable = input("Mensaje que se muestra al usuario: ")

print("="*50)
print("PROGRAMA: Conociendo al usuario")
print("="*50)

nombre = input("¿Cómo te llamas? ")
# Ahora "nombre" tiene lo que el usuario escribió.
print(f"¡Hola, {nombre}! ¡Bienvenido al curso de Python!")

ciudad = input("¿En qué ciudad vives? ")
print(f"¡Qué bueno! {ciudad} es una ciudad genial.")

# ============================================================
# SECCIÓN 2: CONVERTIR TEXTO A NÚMERO
# ============================================================

# IMPORTANTE: input() SIEMPRE devuelve texto (str), incluso si el
# usuario escribe "25". Para hacer matemáticas, hay que convertirlo.

# int()   → convierte a número entero (sin decimales)
# float() → convierte a número decimal

edad_texto = input("¿Cuántos años tienes? ")
# edad_texto ahora es un str, como "25"

edad = int(edad_texto)  # Convertimos "25" (str) a 25 (int)
# Ahora podemos hacer matemáticas con "edad"

print(f"Tienes {edad} años.")
print(f"En 10 años tendrás {edad + 10} años.")
print(f"Has vivido aproximadamente {edad * 365} días.")

# Forma abreviada (todo en una línea):
# edad = int(input("¿Cuántos años tienes? "))

# Para decimales, usa float():
altura = float(input("¿Cuánto mides en metros? (ejemplo: 1.75) "))
print(f"Mides {altura} metros, que son {altura * 100} centímetros.")

# ============================================================
# SECCIÓN 3: OPERADORES ARITMÉTICOS
# ============================================================

print("\n--- TODOS LOS OPERADORES ---")

a = 17
b = 5

print(f"a = {a}, b = {b}")
print(f"Suma:              a + b  = {a + b}")      # 22
print(f"Resta:             a - b  = {a - b}")      # 12
print(f"Multiplicación:    a * b  = {a * b}")      # 85
print(f"División:          a / b  = {a / b}")      # 3.4 (siempre da decimal)
print(f"División entera:   a // b = {a // b}")     # 3   (descarta decimales)
print(f"Módulo (resto):    a % b  = {a % b}")      # 2   (el residuo de 17/5)
print(f"Potencia:          a ** b = {a ** b}")     # 17^5 = 1419857

# ¿Para qué sirve el módulo (%)?
# Es muy útil para saber si un número es par o impar:
# Si numero % 2 == 0 → es par
# Si numero % 2 == 1 → es impar
print(f"\n17 % 2 = {17 % 2} → 17 es impar")
print(f"18 % 2 = {18 % 2} → 18 es par")

# ============================================================
# SECCIÓN 4: ORDEN DE OPERACIONES
# ============================================================

# Python sigue el orden matemático: primero * y /, luego + y -
# Usa paréntesis () para cambiar el orden

resultado1 = 2 + 3 * 4      # Primero 3*4=12, luego 2+12=14
resultado2 = (2 + 3) * 4    # Primero (2+3)=5, luego 5*4=20

print(f"\n2 + 3 * 4 = {resultado1}   (sin paréntesis)")
print(f"(2 + 3) * 4 = {resultado2}  (con paréntesis)")

# ============================================================
# SECCIÓN 5: CALCULADORA SIMPLE
# ============================================================

print("\n" + "="*50)
print("CALCULADORA SIMPLE")
print("="*50)

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print(f"\nResultados con {num1} y {num2}:")
print(f"  {num1} + {num2} = {num1 + num2}")
print(f"  {num1} - {num2} = {num1 - num2}")
print(f"  {num1} * {num2} = {num1 * num2}")

# Evitamos dividir por cero (por ahora, más adelante aprenderemos mejor forma)
if num2 != 0:
    print(f"  {num1} / {num2} = {num1 / num2:.2f}")  # :.2f → 2 decimales
else:
    print("  División: no se puede dividir por cero")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Conversor de Celsius a Fahrenheit
# ────────────────────────────────────────────────
# Pide al usuario una temperatura en Celsius.
# Conviértela a Fahrenheit con la fórmula: F = C * 9/5 + 32
# Muestra el resultado con f-string.
# Ejemplo: "25°C = 77.0°F"
#
# PISTA: temperatura_c = float(input("Temperatura en Celsius: "))
#        temperatura_f = temperatura_c * 9/5 + 32
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Calculadora de IMC
# ─────────────────────────────────
# El IMC (Índice de Masa Corporal) se calcula así: IMC = peso / (altura ** 2)
# Pide al usuario su peso (en kg) y su altura (en metros).
# Calcula y muestra el IMC con 2 decimales.
# Ejemplo: "Tu IMC es: 22.86"
#
# PISTA: usa float(input(...)) para pedir los datos
#        el operador ** eleva a una potencia
#        :.2f dentro del f-string muestra 2 decimales
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Calculadora de vuelto
# ────────────────────────────────────
# Simula una tienda. Pide:
#   - El precio de un producto
#   - La cantidad de dinero con que paga el cliente
# Calcula y muestra el vuelto (cambio).
# Si el cliente no pagó suficiente, muestra "Dinero insuficiente".
#
# PISTA: vuelto = dinero_pagado - precio
#        Puedes usar if/else para el caso de dinero insuficiente
#        (los if/else los verás mejor el día 6, pero puedes intentarlo)
#
# ESCRIBE TU CÓDIGO AQUÍ:
