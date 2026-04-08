# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 7: BUCLE WHILE — REPETIR MIENTRAS...             ║
# ║  Fase 2: Control de Flujo                               ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es un bucle y para qué sirve
#    - Bucle while: repite mientras una condición sea True
#    - break: salir del bucle antes de tiempo
#    - continue: saltar a la siguiente repetición
#    - Cómo hacer menús interactivos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Sigue las instrucciones en pantalla
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con los bucles
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia06_condicionales.py
# ⏭️ SIGUIENTE: dia08_for.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UN BUCLE?
# ============================================================

# Un bucle es una instrucción que se repite.
# Imagina que tienes que escribir "Hola" 100 veces.
# Sin bucle: print("Hola") × 100 líneas (¡horrible!)
# Con bucle: 3 líneas de código

# El bucle WHILE repite mientras una condición sea True:
#
# while condicion:
#     código que se repite

# Ejemplo simple: contador del 1 al 5
print("Contando del 1 al 5:")
contador = 1
while contador <= 5:
    print(f"  Número: {contador}")
    contador = contador + 1  # MUY IMPORTANTE: actualizar el contador
print("¡Listo!\n")

# ⚠️ PELIGRO — BUCLE INFINITO:
# Si olvidas actualizar el contador, el bucle nunca termina.
# Si eso pasa, presiona Ctrl+C para detener el programa.

# ============================================================
# SECCIÓN 2: break — SALIR DEL BUCLE
# ============================================================

# break interrumpe el bucle inmediatamente, aunque la condición sea True.

print("Buscando el número 7:")
numero = 0
while True:  # Este bucle sería infinito...
    numero += 1
    if numero == 7:
        print(f"  ¡Encontré el 7!")
        break  # ...pero break lo detiene cuando número es 7
print("Salí del bucle.\n")

# ============================================================
# SECCIÓN 3: continue — SALTAR UNA ITERACIÓN
# ============================================================

# continue salta el resto del código en esa repetición y va a la siguiente.

print("Números del 1 al 10, saltando los pares:")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Si es par, salta al siguiente número
    print(f"  {i}")  # Solo imprime los impares
print()

# ============================================================
# SECCIÓN 4: ADIVINA EL NÚMERO
# ============================================================

import random  # Módulo para generar números aleatorios

print("="*45)
print("JUEGO: ADIVINA EL NÚMERO")
print("="*45)
print("Estoy pensando en un número del 1 al 20...")

numero_secreto = random.randint(1, 20)  # Número aleatorio entre 1 y 20
intentos = 0
max_intentos = 5

while intentos < max_intentos:
    intentos += 1
    intento = int(input(f"\nIntento {intentos}/{max_intentos}. Tu número: "))

    if intento == numero_secreto:
        print(f"🎉 ¡CORRECTO! Era el {numero_secreto}. Lo adivinaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("📈 Demasiado bajo, prueba con uno mayor.")
    else:
        print("📉 Demasiado alto, prueba con uno menor.")
else:
    # Este else se ejecuta cuando el while termina SIN que se ejecute break
    print(f"\n😔 Se acabaron los intentos. El número era {numero_secreto}.")

# ============================================================
# SECCIÓN 5: MENÚ INTERACTIVO
# ============================================================

print("\n" + "="*45)
print("MENÚ INTERACTIVO")
print("="*45)

dinero = 100  # Empezamos con $100

while True:
    print(f"\n💰 Tu dinero: ${dinero}")
    print("1. Ganar $50")
    print("2. Gastar $30")
    print("3. Ver saldo")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        dinero += 50
        print("✅ Ganaste $50")
    elif opcion == "2":
        if dinero >= 30:
            dinero -= 30
            print("✅ Gastaste $30")
        else:
            print("❌ No tienes suficiente dinero")
    elif opcion == "3":
        print(f"Tu saldo actual es: ${dinero}")
    elif opcion == "4":
        print(f"Saliendo... Saldo final: ${dinero}")
        break
    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Cuenta regresiva
# ──────────────────────────────
# Pide al usuario un número y haz una cuenta regresiva
# desde ese número hasta 0, imprimiendo cada número.
# Al llegar a 0, imprime "¡DESPEGUE! 🚀"
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Sumar hasta que el usuario escriba 0
# ──────────────────────────────────────────────────
# Pide números al usuario uno por uno.
# Ve sumando cada número que ingrese.
# Cuando escriba 0, muestra la suma total.
# Ejemplo: escribe 5, luego 3, luego 7, luego 0 → "Total: 15"
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Piedra, Papel o Tijera
# ─────────────────────────────────────
# Crea un juego de piedra/papel/tijera contra la computadora.
# La computadora elige aleatoriamente con random.choice(['piedra','papel','tijera'])
# El usuario elige. Determina quién gana.
# Pregunta si quieren jugar de nuevo.
#
# PISTA: piedra gana a tijera, tijera gana a papel, papel gana a piedra
#
# ESCRIBE TU CÓDIGO AQUÍ:
