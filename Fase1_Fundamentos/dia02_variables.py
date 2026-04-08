# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 2: VARIABLES — GUARDAR INFORMACIÓN               ║
# ║  Fase 1: Fundamentos                                    ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es una variable y para qué sirve
#    - Tipos de datos: int, float, str, bool
#    - Cómo ver el tipo de una variable con type()
#    - Cómo cambiar el valor de una variable
#    - Cómo combinar texto y variables
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Modifica los valores y experimenta
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia01_hola_mundo.py
# ⏭️ SIGUIENTE: dia03_entrada_operadores.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UNA VARIABLE?
# ============================================================

# Una variable es como una caja con etiqueta donde guardas información.
# La "etiqueta" es el nombre de la variable.
# Lo que guardas adentro es el "valor".

# Para crear una variable, escribes: nombre = valor
# El símbolo = significa "guarda este valor en esta variable"
# (No es el igual matemático, es una ASIGNACIÓN)

nombre = "María"   # Creamos una variable llamada "nombre" con valor "María"
edad = 25          # Variable "edad" con el número 25
altura = 1.75      # Variable "altura" con el número 1.75

# Ahora podemos usar estas variables en print():
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)

# ============================================================
# SECCIÓN 2: TIPOS DE DATOS
# ============================================================

# Python tiene 4 tipos básicos de datos:

# 1. int (número entero — sin decimales)
mi_edad = 25
numero_hermanos = 3
año_nacimiento = 2000
print("\n--- ENTEROS (int) ---")
print("Mi edad:", mi_edad)
print("Número de hermanos:", numero_hermanos)

# 2. float (número decimal — con punto, NO con coma)
mi_altura = 1.75
temperatura = 36.6
precio = 9.99
print("\n--- DECIMALES (float) ---")
print("Mi altura:", mi_altura)
print("Temperatura corporal:", temperatura)

# 3. str (string / texto — siempre entre comillas)
mi_nombre = "Carlos"
mi_ciudad = "Buenos Aires"
mi_color_favorito = "azul"
print("\n--- TEXTO (str) ---")
print("Mi nombre:", mi_nombre)
print("Mi ciudad:", mi_ciudad)

# 4. bool (booleano — solo puede ser True o False)
# True = verdadero, False = falso
# Nota: la primera letra es MAYÚSCULA siempre
soy_estudiante = True
tengo_coche = False
es_fin_de_semana = False
print("\n--- BOOLEANOS (bool) ---")
print("¿Soy estudiante?", soy_estudiante)
print("¿Tengo coche?", tengo_coche)

# ============================================================
# SECCIÓN 3: VER EL TIPO DE UNA VARIABLE CON type()
# ============================================================

# La función type() te dice qué tipo de dato es una variable:
print("\n--- TIPOS DE DATOS ---")
print("Tipo de mi_nombre:", type(mi_nombre))         # <class 'str'>
print("Tipo de mi_edad:", type(mi_edad))             # <class 'int'>
print("Tipo de mi_altura:", type(mi_altura))         # <class 'float'>
print("Tipo de soy_estudiante:", type(soy_estudiante))  # <class 'bool'>

# ============================================================
# SECCIÓN 4: CAMBIAR EL VALOR DE UNA VARIABLE
# ============================================================

# Una variable puede cambiar su valor en cualquier momento.
# (Por eso se llama "variable" — porque varía)

puntos = 0                    # Empieza en 0
print("\nPuntos iniciales:", puntos)

puntos = 10                   # Ahora vale 10
print("Después de la primera misión:", puntos)

puntos = puntos + 5           # Le sumamos 5 a lo que ya tiene
print("Después de la segunda misión:", puntos)

puntos = puntos * 2           # Lo multiplicamos por 2
print("Después de bonus x2:", puntos)

# Forma abreviada de sumar/restar/multiplicar/dividir:
puntos += 3    # Es lo mismo que: puntos = puntos + 3
print("Después de +3:", puntos)

puntos -= 2    # Es lo mismo que: puntos = puntos - 2
print("Después de -2:", puntos)

# ============================================================
# SECCIÓN 5: CONCATENAR TEXTO (UNIR STRINGS)
# ============================================================

# Puedes unir textos con el símbolo +:
saludo = "Hola, " + "mundo"
print("\n" + saludo)

# También puedes unir variables de tipo str:
nombre_completo = "Ana" + " " + "García"
print("Nombre completo:", nombre_completo)

# ============================================================
# SECCIÓN 6: f-STRINGS (LA FORMA MÁS MODERNA Y FÁCIL)
# ============================================================

# Los f-strings son la mejor forma de combinar texto y variables.
# Solo escribe f"..." y dentro usa {nombre_variable}

nombre = "Lucía"
edad = 22
ciudad = "Madrid"
altura = 1.68

# Sin f-string (más complicado):
print("Me llamo", nombre, "tengo", edad, "años y vivo en", ciudad)

# Con f-string (mucho más fácil y legible):
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

# También puedes hacer operaciones dentro de las llaves:
print(f"El año que viene tendré {edad + 1} años")
print(f"Mi altura en centímetros es {altura * 100} cm")

# ============================================================
# SECCIÓN 7: EJEMPLO PRÁCTICO — DATOS DE UNA PERSONA
# ============================================================

print("\n" + "="*40)
print("FICHA PERSONAL")
print("="*40)

persona_nombre = "Roberto"
persona_apellido = "González"
persona_edad = 30
persona_altura = 1.80
persona_ciudad = "Monterrey"
persona_es_programador = True

print(f"Nombre completo: {persona_nombre} {persona_apellido}")
print(f"Edad: {persona_edad} años")
print(f"Altura: {persona_altura} metros")
print(f"Ciudad: {persona_ciudad}")
print(f"¿Es programador? {persona_es_programador}")
print(f"Edad en meses: {persona_edad * 12}")
print(f"Edad en días (aprox): {persona_edad * 365}")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Tus datos personales
# ───────────────────────────────────
# Crea variables con TUS datos y muéstralos con f-strings:
#   - tu_nombre (str)
#   - tu_edad (int)
#   - tu_altura (float, en metros, ej: 1.70)
#   - tu_ciudad (str)
#   - tienes_mascota (bool)
#
# Ejemplo de salida:
#   Hola, me llamo Pedro, tengo 28 años
#   Vivo en Caracas y mido 1.73 metros
#   ¿Tengo mascota? True
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Área de un rectángulo
# ────────────────────────────────────
# Crea variables para el ancho (5) y alto (3) de un rectángulo.
# Calcula el área (ancho * alto) y guárdala en otra variable.
# Muestra el resultado con un f-string.
# Ejemplo: "Un rectángulo de 5 x 3 tiene un área de 15"
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Convertir edad a meses y días
# ───────────────────────────────────────────
# Crea una variable "mi_edad" con tu edad.
# Calcula y muestra:
#   - Tu edad en meses (multiplicar por 12)
#   - Tu edad en días aproximados (multiplicar por 365)
#   - Tu edad en horas aproximadas (multiplicar por 365 * 24)
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 4: Verifica los tipos
# ────────────────────────────────
# Crea una variable de cada tipo (int, float, str, bool)
# y usa type() para mostrar su tipo.
# Ejemplo: print(type(mi_variable))
#
# ESCRIBE TU CÓDIGO AQUÍ:
