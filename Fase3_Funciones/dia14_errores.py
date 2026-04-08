# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 14: MANEJO DE ERRORES — try / except             ║
# ║  Fase 3: Funciones                                      ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué son los errores (excepciones) en Python
#    - try, except, else, finally
#    - Tipos de errores: ZeroDivisionError, ValueError, etc.
#    - Cómo hacer funciones robustas que no fallen
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Prueba con entradas incorrectas para ver el manejo
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia13_modulos.py
# ⏭️ SIGUIENTE: dia15_proyecto_quiz.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ SON LOS ERRORES?
# ============================================================

# Cuando Python encuentra algo que no puede ejecutar, "lanza" una excepción.
# Si no la manejamos, el programa se detiene abruptamente.
#
# Ejemplo de error sin manejar:
# numero = int("hola")  ← ValueError: invalid literal for int()
# resultado = 10 / 0    ← ZeroDivisionError: division by zero
#
# Con try/except, podemos "atrapar" el error y manejarlo elegantemente:
#
# try:
#     código que podría fallar
# except TipoDeError:
#     qué hacer si falla
# else:
#     qué hacer si NO falla (opcional)
# finally:
#     esto SIEMPRE se ejecuta, falle o no (opcional)

# ============================================================
# SECCIÓN 2: TRY / EXCEPT BÁSICO
# ============================================================

print("--- Ejemplo: división segura ---")
try:
    numero = int(input("Escribe un número para dividir 100: "))
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")
except ZeroDivisionError:
    print("❌ Error: No puedes dividir por cero")
except ValueError:
    print("❌ Error: Eso no es un número válido")

# ============================================================
# SECCIÓN 3: MÚLTIPLES EXCEPCIONES
# ============================================================

print("\n--- Tipos de errores comunes ---")

# ZeroDivisionError: división por cero
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError atrapado: {e}")

# ValueError: valor incorrecto (ej: convertir texto a número)
try:
    numero = int("esto no es un número")
except ValueError as e:
    print(f"ValueError atrapado: {e}")

# TypeError: tipo de dato incorrecto
try:
    resultado = "hola" + 5
except TypeError as e:
    print(f"TypeError atrapado: {e}")

# IndexError: índice fuera de rango
try:
    lista = [1, 2, 3]
    elemento = lista[10]  # No existe índice 10
except IndexError as e:
    print(f"IndexError atrapado: {e}")

# KeyError: clave no existe en diccionario
try:
    persona = {"nombre": "Ana"}
    telefono = persona["telefono"]  # No existe esta clave
except KeyError as e:
    print(f"KeyError atrapado: {e}")

# FileNotFoundError: archivo no existe
try:
    with open("archivo_que_no_existe.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError atrapado: {e}")

# ============================================================
# SECCIÓN 4: else Y finally
# ============================================================

print("\n--- try / except / else / finally ---")

try:
    numero = int(input("Escribe un número entero: "))
    resultado = 100 / numero

except ZeroDivisionError:
    print("❌ No se puede dividir por cero")
except ValueError:
    print("❌ Eso no es un número")

else:
    # Solo se ejecuta si NO hubo excepción
    print(f"✅ Resultado: 100 / {numero} = {resultado:.2f}")

finally:
    # Siempre se ejecuta, sin importar si hubo error o no
    print("ℹ️  (Este mensaje siempre aparece)")

# ============================================================
# SECCIÓN 5: FUNCIÓN ROBUSTA PARA PEDIR NÚMEROS
# ============================================================

def pedir_numero(mensaje, tipo=int, minimo=None, maximo=None):
    """
    Pide un número al usuario de forma segura.
    Repite hasta que el usuario ingrese un número válido.
    """
    while True:
        try:
            valor = tipo(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"❌ El número debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"❌ El número debe ser menor o igual a {maximo}")
                continue

            return valor

        except ValueError:
            print(f"❌ Por favor escribe un número válido")

# Usando la función:
print("\n--- Función pedir_numero ---")
edad = pedir_numero("¿Cuántos años tienes? (1-120): ", int, 1, 120)
print(f"Edad registrada: {edad}")

# ============================================================
# SECCIÓN 6: CALCULADORA ROBUSTA
# ============================================================

print("\n" + "="*45)
print("CALCULADORA CON MANEJO DE ERRORES")
print("="*45)

def calculadora_segura():
    """Calculadora que maneja todos los posibles errores."""
    print("\nOperaciones: +, -, *, /")

    while True:
        try:
            num1 = float(input("Primer número: "))
            operacion = input("Operación (+, -, *, /): ").strip()
            num2 = float(input("Segundo número: "))

            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero")
                resultado = num1 / num2
            else:
                raise ValueError(f"Operación '{operacion}' no reconocida")

            print(f"✅ Resultado: {num1} {operacion} {num2} = {resultado}")

        except ValueError as e:
            print(f"❌ Error de valor: {e}")
        except ZeroDivisionError as e:
            print(f"❌ Error matemático: {e}")

        continuar = input("\n¿Otro cálculo? (s/n): ").lower()
        if continuar != "s":
            break

    print("Calculadora cerrada.")

calculadora_segura()

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Calculadora con validación
# ────────────────────────────────────────
# Crea una calculadora que:
# - Use try/except para capturar entradas no numéricas
# - Maneje la división por cero
# - Permita al usuario hacer múltiples cálculos
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Función promedio seguro
# ──────────────────────────────────────
# Crea una función promedio_seguro(lista) que:
# - Devuelva el promedio de una lista
# - Si la lista está vacía, lance un ValueError con mensaje claro
# - Si algún elemento no es número, lo ignore y continúe
# Prueba con: [], [1,2,3], [1,"hola",3,True,4]
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Leer archivo con manejo de errores
# ─────────────────────────────────────────────────
# Pide al usuario el nombre de un archivo.
# Intenta abrirlo y leer su contenido.
# Si no existe, muestra un mensaje amigable.
# Si existe, muestra cuántas líneas y palabras tiene.
# PISTA: usa open() con try/except FileNotFoundError
#
# ESCRIBE TU CÓDIGO AQUÍ:
