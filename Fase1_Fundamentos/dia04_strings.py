# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 4: STRINGS — MANIPULACIÓN DE TEXTO               ║
# ║  Fase 1: Fundamentos                                    ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Métodos de strings: .upper(), .lower(), .strip(), .replace()
#    - f-strings avanzados
#    - Indexación: cómo acceder a letras individuales
#    - Slicing: cómo obtener partes de un texto
#    - len(): cómo contar caracteres
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Cambia los textos y experimenta
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia03_entrada_operadores.py
# ⏭️ SIGUIENTE: dia05_proyecto_tarjeta.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: MÉTODOS BÁSICOS DE STRINGS
# ============================================================

# Los strings tienen "métodos" (funciones incorporadas).
# Se usan así: texto.metodo()

frase = "  Hola, Mundo! Bienvenido a Python  "
print("Texto original:", repr(frase))  # repr() muestra los espacios

# .upper() → convierte a MAYÚSCULAS
print("MAYÚSCULAS:", frase.upper())

# .lower() → convierte a minúsculas
print("minúsculas:", frase.lower())

# .strip() → elimina espacios al inicio y al final
print("Sin espacios:", frase.strip())

# .lstrip() y .rstrip() → quitan espacios solo de un lado
print("Sin espacio izquierdo:", frase.lstrip())
print("Sin espacio derecho:", frase.rstrip())

# .replace(viejo, nuevo) → reemplaza texto
nombre = "Hola, Mundo"
print("\nOriginal:", nombre)
print("Reemplazado:", nombre.replace("Mundo", "Python"))
print("En mayúsculas:", nombre.replace("o", "0"))  # Cambia todas las "o" por "0"

# .title() → La Primera Letra De Cada Palabra En Mayúscula
titulo = "el señor de los anillos"
print("\nTítulo:", titulo.title())

# .capitalize() → Solo la primera letra en mayúscula
print("Capitalize:", titulo.capitalize())

# .count(texto) → cuenta cuántas veces aparece algo
frase2 = "python es genial, python es poderoso, python es gratis"
print(f"\n'python' aparece {frase2.count('python')} veces")

# .find(texto) → busca dónde está algo (devuelve posición o -1 si no está)
print(f"'genial' está en la posición: {frase2.find('genial')}")
print(f"'java' está en la posición: {frase2.find('java')}")  # -1 = no encontrado

# ============================================================
# SECCIÓN 2: LEN() — CONTAR CARACTERES
# ============================================================

# len() cuenta el número de caracteres (letras, espacios, etc.)
palabra = "Python"
frase3 = "Hola, mundo"

print(f"\nLongitud de '{palabra}': {len(palabra)}")  # 6
print(f"Longitud de '{frase3}': {len(frase3)}")      # 11 (incluye coma y espacio)

# Útil para verificar contraseñas:
password = "abc123"
if len(password) >= 8:
    print("La contraseña es suficientemente larga")
else:
    print(f"La contraseña es muy corta ({len(password)} caracteres). Mínimo 8.")

# ============================================================
# SECCIÓN 3: INDEXACIÓN — ACCEDER A LETRAS INDIVIDUALES
# ============================================================

# Cada letra de un string tiene una "posición" (índice).
# La primera posición es 0, no 1 (los programadores cuentan desde 0).

#  P  y  t  h  o  n
#  0  1  2  3  4  5   → índices positivos (de izquierda a derecha)
# -6 -5 -4 -3 -2 -1   → índices negativos (de derecha a izquierda)

lenguaje = "Python"
print(f"\nPalabra: {lenguaje}")
print(f"Primera letra (índice 0): {lenguaje[0]}")   # P
print(f"Tercera letra (índice 2): {lenguaje[2]}")   # t
print(f"Última letra (índice -1): {lenguaje[-1]}")  # n
print(f"Penúltima (índice -2): {lenguaje[-2]}")     # o

# ============================================================
# SECCIÓN 4: SLICING — OBTENER PARTES DEL TEXTO
# ============================================================

# El slicing usa la sintaxis: texto[inicio:fin]
# El índice "fin" NO se incluye (es exclusivo)
# Si omites "inicio", empieza desde el principio
# Si omites "fin", llega hasta el final

frase4 = "Hola, Mundo!"
#         0123456789...

print(f"\nTexto completo: {frase4}")
print(f"Primeros 4 caracteres [0:4]: {frase4[0:4]}")   # Hola
print(f"Desde el 6 hasta el 11 [6:11]: {frase4[6:11]}") # Mundo
print(f"Desde el inicio hasta el 5 [:5]: {frase4[:5]}") # Hola,
print(f"Desde el 7 hasta el final [7:]: {frase4[7:]}")  # undo!
print(f"Los últimos 6 [-6:]: {frase4[-6:]}")            # Mundo!

# Con paso (cada N letras):
abecedario = "abcdefghij"
print(f"\nAbecedario: {abecedario}")
print(f"De 2 en 2 [::2]: {abecedario[::2]}")   # acegi
print(f"Al revés [::-1]: {abecedario[::-1]}")   # jihgfedcba

# ============================================================
# SECCIÓN 5: F-STRINGS AVANZADOS
# ============================================================

nombre = "María"
edad = 25
altura = 1.68
precio = 1234567.89

# Formato de números:
print(f"\n--- FORMATO DE NÚMEROS ---")
print(f"Altura con 1 decimal: {altura:.1f}")          # 1.7
print(f"Precio: ${precio:,.2f}")                       # $1,234,567.89
print(f"Porcentaje: {0.856:.1%}")                      # 85.6%
print(f"Número con ceros: {42:05d}")                   # 00042

# Alineación de texto:
print(f"\n--- ALINEACIÓN ---")
print(f"|{'izquierda':<20}|")    # Alinear a la izquierda
print(f"|{'centro':^20}|")       # Centrar
print(f"|{'derecha':>20}|")      # Alinear a la derecha

# ============================================================
# SECCIÓN 6: EJEMPLO PRÁCTICO — GENERADOR DE EMAILS
# ============================================================

print("\n" + "="*50)
print("GENERADOR DE EMAIL CORPORATIVO")
print("="*50)

nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
empresa = input("Nombre de la empresa: ")

# Procesamos los datos:
nombre_limpio = nombre_usuario.strip().lower()
apellido_limpio = apellido_usuario.strip().lower()
empresa_limpia = empresa.strip().lower().replace(" ", "")

# Generamos el email:
email = f"{nombre_limpio}.{apellido_limpio}@{empresa_limpia}.com"

print(f"\nTu email corporativo es: {email}")
print(f"Longitud del email: {len(email)} caracteres")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Transformaciones de texto
# ───────────────────────────────────────
# Pide al usuario una frase.
# Muestra la frase en: MAYÚSCULAS, minúsculas, con la primera
# letra de cada palabra en mayúscula, y al revés.
# Ejemplo si escribe "hola mundo":
#   MAYÚSCULAS: HOLA MUNDO
#   minúsculas: hola mundo
#   Título: Hola Mundo
#   Al revés: odnum aloh
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Contar letras en una palabra
# ──────────────────────────────────────────
# Pide al usuario una palabra.
# Muestra:
#   - Cuántas letras tiene
#   - La primera y última letra
#   - La palabra sin espacios (usa .strip())
#   - Cuántas veces aparece la letra "a" (usa .count())
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Generador de nombres de usuario
# ─────────────────────────────────────────────
# Pide nombre, apellido y año de nacimiento.
# Genera un nombre de usuario así:
#   - Primera letra del nombre + apellido completo + últimos 2 dígitos del año
#   - Todo en minúsculas
# Ejemplo: nombre="Ana", apellido="López", año=1998 → "alopez98"
#
# PISTA: nombre[0] da la primera letra
#        str(año)[-2:] da los últimos 2 dígitos del año
#
# ESCRIBE TU CÓDIGO AQUÍ:
