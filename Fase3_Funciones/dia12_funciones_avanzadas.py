# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 12: FUNCIONES AVANZADAS                          ║
# ║  Fase 3: Funciones                                      ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - lambda: funciones de una sola línea
#    - map() y filter(): aplicar funciones a listas
#    - List comprehensions: crear listas en una línea
#    - *args: parámetros variables
#    - **kwargs: parámetros con nombre variables
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con las funciones lambda
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia11_funciones.py
# ⏭️ SIGUIENTE: dia13_modulos.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: FUNCIONES LAMBDA
# ============================================================

# Una lambda es una función pequeña de una sola línea.
# Sintaxis: lambda parametros: expresion
# Se usa cuando la función es tan simple que no vale la pena darle nombre.

# Función normal:
def doble_normal(x):
    return x * 2

# La misma función como lambda:
doble_lambda = lambda x: x * 2

# Ambas hacen lo mismo:
print(f"Normal: {doble_normal(5)}")     # 10
print(f"Lambda: {doble_lambda(5)}")     # 10

# Lambda con múltiples parámetros:
sumar = lambda a, b: a + b
potencia = lambda base, exp: base ** exp
es_par = lambda n: n % 2 == 0

print(f"\n3 + 7 = {sumar(3, 7)}")
print(f"2^10 = {potencia(2, 10)}")
print(f"¿8 es par? {es_par(8)}")
print(f"¿7 es par? {es_par(7)}")

# ============================================================
# SECCIÓN 2: map() — APLICAR FUNCIÓN A TODOS LOS ELEMENTOS
# ============================================================

# map(funcion, lista) → aplica la función a cada elemento de la lista
# Devuelve un objeto "map", lo convertimos a lista con list()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular el cuadrado de cada número:
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"\nNúmeros: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Convertir temperatura:
temperaturas_celsius = [0, 10, 20, 30, 40, 100]
a_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperaturas_celsius))
print(f"\nCelsius: {temperaturas_celsius}")
print(f"Fahrenheit: {a_fahrenheit}")

# ============================================================
# SECCIÓN 3: filter() — FILTRAR ELEMENTOS
# ============================================================

# filter(funcion, lista) → solo conserva los elementos donde la función devuelve True

numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Solo los pares:
pares = list(filter(lambda x: x % 2 == 0, numeros2))
print(f"\nTodos los números: {numeros2}")
print(f"Solo pares: {pares}")

# Solo los mayores de 7:
mayores_7 = list(filter(lambda x: x > 7, numeros2))
print(f"Mayores de 7: {mayores_7}")

# Filtrar palabras largas:
palabras = ["sol", "mariposa", "luz", "programación", "río", "computadora"]
palabras_largas = list(filter(lambda p: len(p) > 5, palabras))
print(f"\nPalabras: {palabras}")
print(f"Palabras largas (>5 letras): {palabras_largas}")

# ============================================================
# SECCIÓN 4: LIST COMPREHENSIONS — LISTAS EN UNA LÍNEA
# ============================================================

# Una list comprehension es una forma concisa de crear listas.
# Sintaxis: [expresion for variable in iterable if condicion]
# La parte "if condicion" es opcional.

# Forma normal (con for loop):
cuadrados_normal = []
for x in range(1, 11):
    cuadrados_normal.append(x ** 2)

# Mismo resultado con list comprehension:
cuadrados_comp = [x ** 2 for x in range(1, 11)]

print(f"\nCuadrados (normal): {cuadrados_normal}")
print(f"Cuadrados (comprehension): {cuadrados_comp}")
# ¡Exactamente igual pero en UNA línea!

# Con condición (equivale a filter):
pares_comp = [x for x in range(1, 21) if x % 2 == 0]
print(f"\nPares del 1 al 20: {pares_comp}")

# Transformación + filtro:
cubos_impares = [x**3 for x in range(1, 10) if x % 2 != 0]
print(f"Cubos de impares del 1 al 9: {cubos_impares}")

# Con strings:
nombres = ["ana", "CARLOS", "beatriz", "DAVID", "elena"]
nombres_titulo = [n.title() for n in nombres]
print(f"\nNombres corregidos: {nombres_titulo}")

# ============================================================
# SECCIÓN 5: *args — PARÁMETROS VARIABLES
# ============================================================

# *args permite que una función reciba CUALQUIER cantidad de argumentos.
# Dentro de la función, args es una TUPLA con todos los argumentos.

def sumar_todo(*args):
    """Suma todos los números que se le pasen."""
    total = 0
    for numero in args:
        total += numero
    return total

print(f"\nSuma de 1,2,3: {sumar_todo(1, 2, 3)}")
print(f"Suma de 5,10,15,20: {sumar_todo(5, 10, 15, 20)}")
print(f"Suma de 100: {sumar_todo(100)}")

def promedio_variable(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print(f"\nPromedio de 10,20,30: {promedio_variable(10, 20, 30):.2f}")
print(f"Promedio de 5,7,8,9,11: {promedio_variable(5, 7, 8, 9, 11):.2f}")

# ============================================================
# SECCIÓN 6: **kwargs — PARÁMETROS CON NOMBRE VARIABLES
# ============================================================

# **kwargs permite recibir cualquier cantidad de parámetros con nombre.
# Dentro de la función, kwargs es un DICCIONARIO.

def crear_perfil(**kwargs):
    """Crea un perfil con los datos que se pasen."""
    print("\n--- PERFIL ---")
    for clave, valor in kwargs.items():
        print(f"  {clave.capitalize()}: {valor}")

crear_perfil(nombre="Ana", edad=25, ciudad="Bogotá")
crear_perfil(nombre="Carlos", profesion="Programador", hobby="Música", nivel="Avanzado")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Cubos del 1 al 10
# ────────────────────────────────
# Usa una list comprehension para crear una lista con los cubos
# de los números del 1 al 10 (x³).
# Muestra la lista resultante.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Filtrar palabras largas
# ──────────────────────────────────────
# Dada la lista: ["casa", "elefante", "sol", "computadora", "pie", "programar"]
# Usa filter() con lambda para quedarte solo con las palabras de más de 5 letras.
# Luego conviértelas a MAYÚSCULAS con map() y lambda.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Función con promedio variable
# ───────────────────────────────────────────
# Crea una función usando *args que calcule el promedio de
# todos los números que reciba.
# Añade un parámetro opcional "mostrar_detalles=False" que,
# si es True, también muestre el mínimo y máximo.
#
# ESCRIBE TU CÓDIGO AQUÍ:
