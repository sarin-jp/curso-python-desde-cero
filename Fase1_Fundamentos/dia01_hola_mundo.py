# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 1: HOLA MUNDO — TU PRIMER PROGRAMA               ║
# ║  Fase 1: Fundamentos                                    ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Cómo mostrar texto en pantalla con print()
#    - Qué son los comentarios (estas líneas con #)
#    - Cómo hacer operaciones matemáticas básicas
#    - Cómo escribir tu primer programa completo
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo — ahí aparecerá el resultado
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios (las líneas con #)
#    2. Ejecuta el programa con ▶️
#    3. Modifica los textos y vuelve a ejecutar
#    4. Haz los ejercicios del final (busca "EJERCICIOS")
#
# ⏮️ ANTERIOR: (este es el primero, ¡bienvenido!)
# ⏭️ SIGUIENTE: dia02_variables.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: LA FUNCIÓN print()
# ============================================================

# La función print() le dice a Python que muestre algo en pantalla.
# Todo lo que está entre las comillas aparecerá tal cual.

print("¡Hola, Mundo!")
print("Me llamo Python y soy tu nuevo amigo 🐍")

# Puedes imprimir cualquier texto que quieras.
# Nota: las comillas pueden ser simples ' ' o dobles " "
print('Esto también funciona con comillas simples')

# ============================================================
# SECCIÓN 2: QUÉ SON LOS COMENTARIOS
# ============================================================

# Los comentarios son líneas que Python ignora completamente.
# Empiezan con el símbolo # (numeral / almohadilla).
# Se usan para explicar qué hace el código.
# ¡Escribe comentarios siempre! Te ayudarán a recordar qué hiciste.

# Esto es un comentario — Python no lo ejecuta
print("Pero esto sí lo ejecuta")  # También puedes comentar al final de una línea

# ============================================================
# SECCIÓN 3: IMPRIMIR VARIAS LÍNEAS
# ============================================================

# Puedes usar tantos print() como quieras.
# Cada print() empieza en una línea nueva.
print("Línea 1")
print("Línea 2")
print("Línea 3")

# Para imprimir una línea vacía (salto de línea), usa print() sin nada:
print()  # <-- esto imprime una línea en blanco

# ============================================================
# SECCIÓN 4: OPERACIONES MATEMÁTICAS BÁSICAS
# ============================================================

# Python puede hacer matemáticas directamente dentro de print():

print("Suma: 5 + 3 =", 5 + 3)          # Suma
print("Resta: 10 - 4 =", 10 - 4)       # Resta
print("Multiplicación: 6 * 7 =", 6 * 7)  # Multiplicación (usa *)
print("División: 20 / 4 =", 20 / 4)    # División (usa /)
print("División entera: 7 // 2 =", 7 // 2)  # División entera (resultado sin decimales)
print("Resto (módulo): 7 % 2 =", 7 % 2)  # El resto de la división
print("Potencia: 2 ** 8 =", 2 ** 8)     # 2 elevado a la 8 = 256

# ============================================================
# SECCIÓN 5: IMPRIMIR TEXTO Y NÚMEROS JUNTOS
# ============================================================

# La coma (,) en print() permite combinar texto y números:
print("Mi edad es:", 25)
print("El resultado de 100 / 4 es:", 100 / 4)

# También puedes calcular dentro del print():
print("El doble de 15 es:", 15 * 2)
print("¿Cuántos minutos tiene un día?", 24 * 60)
print("¿Cuántos segundos tiene un día?", 24 * 60 * 60)

# ============================================================
# SECCIÓN 6: DIBUJOS CON print()
# ============================================================

# ¡Puedes hacer arte con texto! Se llama "ASCII art":
print()
print("   /|")
print("  / |")
print(" /  |")
print("/   |")
print("----+")
print("Un triángulo hecho con print() 🎨")
print()

print("*****")
print("*   *")
print("*   *")
print("*   *")
print("*****")
print("Un cuadrado con asteriscos")
print()

print("  🐍")
print(" Python")
print("  .--.")
print(" (o  o)")
print(" | -- |")
print("  \\  /")
print("   \\/")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Imprimir tu nombre
# ─────────────────────────────────
# Escribe un print() que muestre tu nombre.
# Ejemplo esperado: "Me llamo Juan"
#
# ESCRIBE TU CÓDIGO AQUÍ:
# print("Me llamo ___")


# EJERCICIO 2: Imprimir tu edad y una operación
# ─────────────────────────────────────────────
# Escribe dos print():
#   - Uno que muestre cuántos años tienes
#   - Otro que calcule cuántos días has vivido (aproximado: edad * 365)
# Ejemplo: "Tengo 20 años" y "He vivido aproximadamente: 7300 días"
#
# ESCRIBE TU CÓDIGO AQUÍ:
# print("Tengo", ___, "años")
# print("He vivido aproximadamente:", ___ * 365, "días")


# EJERCICIO 3: Dibujo con print()
# ────────────────────────────────
# Usa varios print() para dibujar una casa simple con caracteres:
#   /\
#  /  \
# /    \
# |    |
# |    |
# ------
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 4: Calculadora simple
# ────────────────────────────────
# Usa print() para mostrar las siguientes operaciones:
# - La suma de 347 + 589
# - El producto de 24 * 365 (días en un año)
# - El porcentaje: (85 / 100) * 200
#
# PISTA: Escribe el resultado calculado dentro del print(), como:
#        print("347 + 589 =", 347 + 589)
#
# ESCRIBE TU CÓDIGO AQUÍ:


# ============================================================
# 🎉 ¡FELICITACIONES! Completaste el Día 1
# ============================================================
print()
print("════════════════════════════════════")
print("  ¡FELICITACIONES! 🎉")
print("  Completaste el Día 1 del curso.")
print("  Ya escribiste tu primer programa.")
print("  ¡Mañana aprenderás sobre variables!")
print("════════════════════════════════════")
