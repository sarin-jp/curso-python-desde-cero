# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 11: FUNCIONES — BLOQUES REUTILIZABLES            ║
# ║  Fase 3: Funciones                                      ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es una función y por qué usarlas
#    - Cómo crear funciones con def
#    - Parámetros y argumentos
#    - La instrucción return
#    - Valores por defecto en parámetros
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Crea tus propias funciones
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: ../Fase2_Control/dia10_diccionarios.py
# ⏭️ SIGUIENTE: dia12_funciones_avanzadas.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UNA FUNCIÓN?
# ============================================================

# Una función es un bloque de código con nombre que puedes REUTILIZAR.
# En lugar de repetir el mismo código muchas veces,
# lo escribes UNA VEZ como función y la llamas cuando la necesitas.
#
# Analogía: una función es como una receta de cocina.
# Escribes la receta una vez y puedes "ejecutarla" cuando quieras.
#
# Sintaxis:
# def nombre_funcion(parametros):
#     código de la función
#     return valor  ← opcional

# Función más simple (sin parámetros, sin return):
def saludar():
    print("¡Hola! Soy una función.")
    print("Puedo ejecutarme muchas veces.")

# Para LLAMAR (ejecutar) la función:
saludar()   # Primera llamada
saludar()   # Segunda llamada
saludar()   # Tercera llamada
# Con solo 1 línea de código, ejecutamos 3 veces todo lo que está dentro

# ============================================================
# SECCIÓN 2: PARÁMETROS — INFORMACIÓN QUE RECIBE LA FUNCIÓN
# ============================================================

# Los parámetros son variables que la función recibe como "entrada".
# Van entre los paréntesis en la definición.

def saludar_a(nombre):  # "nombre" es el parámetro
    print(f"¡Hola, {nombre}! Bienvenido al curso.")

# Al llamar la función, pasamos el "argumento" (el valor real):
saludar_a("Carlos")      # "Carlos" es el argumento
saludar_a("Ana")
saludar_a("Python")

# Función con múltiples parámetros:
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")

sumar(5, 3)
sumar(100, 200)
sumar(0.5, 1.5)

# ============================================================
# SECCIÓN 3: return — LO QUE LA FUNCIÓN DEVUELVE
# ============================================================

# return hace que la función "devuelva" un valor.
# Ese valor puede guardarse en una variable o usarse directamente.

def multiplicar(a, b):
    return a * b   # La función DEVUELVE el resultado, no lo imprime

# El valor devuelto se puede guardar:
resultado = multiplicar(6, 7)
print(f"\n6 × 7 = {resultado}")

# O usar directamente:
print(f"3 × 4 = {multiplicar(3, 4)}")
print(f"El doble del resultado: {multiplicar(5, 5) * 2}")

# Función que devuelve múltiples valores:
def min_max(lista):
    return min(lista), max(lista)  # Devuelve una tupla

numeros = [3, 1, 4, 1, 5, 9, 2, 6]
minimo, maximo = min_max(numeros)  # "Desempacar" los dos valores
print(f"\nMínimo: {minimo}, Máximo: {maximo}")

# ============================================================
# SECCIÓN 4: VALORES POR DEFECTO
# ============================================================

# Puedes dar valores por defecto a los parámetros.
# Si no se pasa ese argumento, se usa el valor por defecto.

def calcular_precio(precio_base, descuento=0, impuesto=0.16):
    precio_con_descuento = precio_base * (1 - descuento)
    precio_final = precio_con_descuento * (1 + impuesto)
    return precio_final

# Llamadas:
print(f"\nPrecio sin descuento: ${calcular_precio(100):.2f}")
print(f"Precio con 10% descuento: ${calcular_precio(100, 0.10):.2f}")
print(f"Precio con 20% descuento y 8% impuesto: ${calcular_precio(100, 0.20, 0.08):.2f}")

# ============================================================
# SECCIÓN 5: FUNCIONES CON LÓGICA
# ============================================================

def estadisticas(lista):
    """Calcula estadísticas de una lista de números."""
    # (Las comillas triples son la "docstring": descripción de la función)
    if len(lista) == 0:
        return None

    return {
        "cantidad": len(lista),
        "suma": sum(lista),
        "promedio": sum(lista) / len(lista),
        "maximo": max(lista),
        "minimo": min(lista)
    }

notas = [85, 92, 78, 95, 88, 72, 96, 84, 90, 87]
stats = estadisticas(notas)

print("\n--- Estadísticas de notas ---")
print(f"Cantidad de estudiantes: {stats['cantidad']}")
print(f"Promedio: {stats['promedio']:.1f}")
print(f"Nota más alta: {stats['maximo']}")
print(f"Nota más baja: {stats['minimo']}")

# ============================================================
# SECCIÓN 6: EJEMPLO PRÁCTICO — CALCULADORA CON FUNCIONES
# ============================================================

def sumar_f(a, b):
    return a + b

def restar_f(a, b):
    return a - b

def multiplicar_f(a, b):
    return a * b

def dividir_f(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

print("\n" + "="*40)
print("CALCULADORA CON FUNCIONES")
print("="*40)

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

print(f"\n{num1} + {num2} = {sumar_f(num1, num2)}")
print(f"{num1} - {num2} = {restar_f(num1, num2)}")
print(f"{num1} × {num2} = {multiplicar_f(num1, num2)}")
print(f"{num1} ÷ {num2} = {dividir_f(num1, num2)}")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Área de un círculo
# ────────────────────────────────
# Crea una función llamada area_circulo(radio) que devuelva
# el área de un círculo. Fórmula: π × radio²
# PISTA: import math y usa math.pi para el valor de π
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: ¿Es número primo?
# ───────────────────────────────
# Crea una función es_primo(numero) que devuelva True si
# el número es primo, y False si no lo es.
# Un número es primo si solo es divisible por 1 y por sí mismo.
# Prueba con: 2, 3, 4, 7, 10, 13, 17
# PISTA: verifica si numero % i == 0 para i en range(2, numero)
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Conversor de temperaturas
# ────────────────────────────────────────
# Crea tres funciones:
#   celsius_a_fahrenheit(c) → retorna c * 9/5 + 32
#   fahrenheit_a_celsius(f) → retorna (f - 32) * 5/9
#   celsius_a_kelvin(c)     → retorna c + 273.15
# Pruébalas con 0°C, 100°C, -40°C
#
# ESCRIBE TU CÓDIGO AQUÍ:
