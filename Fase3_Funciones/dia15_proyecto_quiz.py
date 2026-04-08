# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 15: PROYECTO — QUIZ INTERACTIVO                  ║
# ║  Fase 3: Funciones                                      ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Aplicar funciones, módulos y manejo de errores
#    - Usar random.shuffle() para preguntas aleatorias
#    - Calcular porcentajes y puntuaciones
#    - Construir un juego interactivo completo
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Responde las preguntas del quiz
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código
#    2. Ejecuta el programa
#    3. Agrega tus propias preguntas al quiz
#    4. Haz los ejercicios de personalización
#
# ⏮️ ANTERIOR: dia14_errores.py
# ⏭️ SIGUIENTE: ../Fase4_POO/dia16_clases.py
# ════════════════════════════════════════════════════════════

import random
import datetime

# ============================================================
# SECCIÓN 1: BANCO DE PREGUNTAS
# ============================================================

# Cada pregunta es un diccionario con:
#   - "pregunta": el texto de la pregunta
#   - "opciones": lista con las opciones (a, b, c, d)
#   - "respuesta": la letra correcta
#   - "explicacion": por qué esa es la respuesta

PREGUNTAS = [
    {
        "pregunta": "¿Cuál función usamos para mostrar texto en pantalla en Python?",
        "opciones": ["a) input()", "b) print()", "c) show()", "d) display()"],
        "respuesta": "b",
        "explicacion": "print() es la función para mostrar texto. input() es para pedir datos."
    },
    {
        "pregunta": "¿Cómo se llama el tipo de dato para texto en Python?",
        "opciones": ["a) text", "b) char", "c) str", "d) string"],
        "respuesta": "c",
        "explicacion": "str (abreviatura de string) es el tipo de dato para texto en Python."
    },
    {
        "pregunta": "¿Cuál es el resultado de: 10 % 3 ?",
        "opciones": ["a) 3", "b) 3.33", "c) 1", "d) 0"],
        "respuesta": "c",
        "explicacion": "% es el operador módulo (resto). 10 ÷ 3 = 3 con resto 1."
    },
    {
        "pregunta": "¿Cuál es el índice del primer elemento de una lista?",
        "opciones": ["a) 1", "b) -1", "c) 0", "d) Ninguno"],
        "respuesta": "c",
        "explicacion": "En Python (y casi todos los lenguajes), los índices empiezan en 0."
    },
    {
        "pregunta": "¿Qué hace la instrucción 'break' dentro de un bucle?",
        "opciones": [
            "a) Pausa el bucle 1 segundo",
            "b) Sale del bucle inmediatamente",
            "c) Salta a la siguiente iteración",
            "d) Reinicia el bucle"
        ],
        "respuesta": "b",
        "explicacion": "break termina el bucle. continue salta a la siguiente iteración."
    },
    {
        "pregunta": "¿Cómo se define una función en Python?",
        "opciones": ["a) function nombre():", "b) func nombre():", "c) def nombre():", "d) define nombre():"],
        "respuesta": "c",
        "explicacion": "def es la palabra clave para definir funciones en Python."
    },
    {
        "pregunta": "¿Qué tipo de dato devuelve siempre input()?",
        "opciones": ["a) int", "b) float", "c) bool", "d) str"],
        "respuesta": "d",
        "explicacion": "input() SIEMPRE devuelve str (texto). Usa int() o float() para convertir."
    },
    {
        "pregunta": "¿Cuál es la forma correcta de un f-string?",
        "opciones": [
            "a) f('Hola {nombre}')",
            "b) f\"Hola {nombre}\"",
            "c) \"Hola\" + {nombre}",
            "d) format(\"Hola nombre\")"
        ],
        "respuesta": "b",
        "explicacion": "Los f-strings van precedidos de f y las variables entre llaves {variable}."
    },
    {
        "pregunta": "¿Qué método agrega un elemento al final de una lista?",
        "opciones": ["a) .add()", "b) .push()", "c) .insert()", "d) .append()"],
        "respuesta": "d",
        "explicacion": "list.append(elemento) agrega al final. insert(posicion, elemento) en posición específica."
    },
    {
        "pregunta": "¿Para qué sirve try/except en Python?",
        "opciones": [
            "a) Probar código nuevo",
            "b) Manejar errores sin que el programa falle",
            "c) Ejecutar código en paralelo",
            "d) Importar módulos"
        ],
        "respuesta": "b",
        "explicacion": "try/except permite capturar errores y manejarlos de forma elegante."
    }
]

# ============================================================
# SECCIÓN 2: FUNCIONES DEL QUIZ
# ============================================================

def mostrar_bienvenida(nombre):
    """Muestra el mensaje de bienvenida del quiz."""
    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + "  🧠 QUIZ DE PYTHON — PON A PRUEBA TU SABER  ".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print(f"\n¡Hola, {nombre}! 👋")
    print("Este quiz tiene preguntas sobre Python.")
    print("Lee cada pregunta y escribe la letra de tu respuesta (a, b, c o d).")
    print()


def hacer_pregunta(pregunta_data, numero, total):
    """Muestra una pregunta y devuelve True si la respuesta es correcta."""
    print(f"\n── Pregunta {numero}/{total} " + "─"*30)
    print(f"❓ {pregunta_data['pregunta']}")
    print()

    for opcion in pregunta_data["opciones"]:
        print(f"   {opcion}")

    # Pedir respuesta válida:
    while True:
        respuesta = input("\nTu respuesta (a/b/c/d): ").strip().lower()
        if respuesta in ["a", "b", "c", "d"]:
            break
        print("❌ Por favor escribe solo a, b, c o d")

    # Verificar:
    es_correcta = (respuesta == pregunta_data["respuesta"])

    if es_correcta:
        print("✅ ¡CORRECTO!")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {pregunta_data['respuesta'].upper()}")

    print(f"💡 Explicación: {pregunta_data['explicacion']}")

    return es_correcta


def calcular_calificacion(puntos, total):
    """Determina la calificación según el puntaje."""
    porcentaje = (puntos / total) * 100

    if porcentaje == 100:
        return "🏆 ¡PERFECTO! ¡Eres un experto en Python!"
    elif porcentaje >= 80:
        return "⭐ ¡Excelente! Dominas muy bien los conceptos."
    elif porcentaje >= 60:
        return "👍 Bien hecho. Repasa los temas donde fallaste."
    elif porcentaje >= 40:
        return "📚 Regular. Vuelve a leer los archivos anteriores."
    else:
        return "💪 Sigue practicando. ¡Cada intento te hace mejorar!"


def mostrar_resultados(nombre, puntos, total, tiempo_segundos, incorrectas):
    """Muestra el resumen final del quiz."""
    porcentaje = (puntos / total) * 100

    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + "  📊 RESULTADOS FINALES  ".center(48) + "║")
    print("╠" + "═"*48 + "╣")
    print(f"║  Jugador: {nombre:<37}║")
    print(f"║  Respuestas correctas: {puntos}/{total}{' '*25}║")
    print(f"║  Porcentaje: {porcentaje:.0f}%{' '*32}║")
    print(f"║  Tiempo: {tiempo_segundos:.0f} segundos{' '*30}║")
    print("╠" + "═"*48 + "╣")

    calificacion = calcular_calificacion(puntos, total)
    print(f"║  {calificacion:<46}║")
    print("╚" + "═"*48 + "╝")

    if incorrectas:
        print(f"\n📋 Preguntas que debes repasar ({len(incorrectas)}):")
        for i, preg in enumerate(incorrectas, 1):
            print(f"  {i}. {preg['pregunta'][:60]}...")


# ============================================================
# SECCIÓN 3: EJECUCIÓN DEL QUIZ
# ============================================================

def main():
    """Función principal que ejecuta el quiz."""
    nombre = input("¿Cuál es tu nombre? ").strip().title()
    mostrar_bienvenida(nombre)

    # Seleccionar y mezclar preguntas:
    num_preguntas = min(5, len(PREGUNTAS))  # Máximo 5 preguntas
    preguntas_seleccionadas = random.sample(PREGUNTAS, num_preguntas)

    puntos = 0
    incorrectas = []
    inicio = datetime.datetime.now()

    # Hacer cada pregunta:
    for i, pregunta in enumerate(preguntas_seleccionadas, 1):
        correcto = hacer_pregunta(pregunta, i, num_preguntas)
        if correcto:
            puntos += 1
        else:
            incorrectas.append(pregunta)

    # Calcular tiempo:
    fin = datetime.datetime.now()
    tiempo = (fin - inicio).total_seconds()

    # Mostrar resultados:
    mostrar_resultados(nombre, puntos, num_preguntas, tiempo, incorrectas)

    # ¿Jugar de nuevo?
    print()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        main()
    else:
        print("\n" + "="*50)
        print("🎉 ¡FELICITACIONES! Completaste la FASE 3: Funciones")
        print("   En la Fase 4 aprenderás Programación Orientada a Objetos.")
        print("="*50)


# Iniciar el quiz:
main()
