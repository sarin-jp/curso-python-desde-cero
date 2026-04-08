# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 5: PROYECTO — TARJETA DE PRESENTACIÓN DIGITAL    ║
# ║  Fase 1: Fundamentos                                    ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Aplicar todo lo aprendido en la Fase 1
#    - Usar input(), variables, f-strings, strings
#    - Crear un programa completo y profesional
#    - Formatear la salida con bordes y colores de texto
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Responde las preguntas que aparecen
#    4. ¡Admira tu tarjeta de presentación!
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa y responde las preguntas
#    3. Personaliza los mensajes y el diseño
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia04_strings.py
# ⏭️ SIGUIENTE: ../Fase2_Control/dia06_condicionales.py
# ════════════════════════════════════════════════════════════

# ============================================================
# PROYECTO: TARJETA DE PRESENTACIÓN DIGITAL
# ============================================================
# Este es tu primer proyecto real. Un programa que pide datos
# al usuario y genera una tarjeta de presentación formateada.

print("╔══════════════════════════════════════════╗")
print("║   GENERADOR DE TARJETA DE PRESENTACIÓN  ║")
print("╚══════════════════════════════════════════╝")
print()
print("Voy a hacerte algunas preguntas para crear")
print("tu tarjeta de presentación digital. 📇")
print()

# ============================================================
# PASO 1: RECOPILAR INFORMACIÓN DEL USUARIO
# ============================================================

nombre = input("¿Cuál es tu nombre? ").strip()
apellido = input("¿Cuál es tu apellido? ").strip()
edad = int(input("¿Cuántos años tienes? "))
profesion = input("¿Cuál es tu profesión o lo que estudias? ").strip()
ciudad = input("¿En qué ciudad vives? ").strip()
pais = input("¿En qué país? ").strip()
email = input("¿Cuál es tu email? ").strip().lower()
habilidad1 = input("¿Cuál es una habilidad que tienes? ").strip()
habilidad2 = input("¿Y otra habilidad? ").strip()
frase = input("Escribe una frase que te defina (corta): ").strip()

# ============================================================
# PASO 2: PROCESAR Y VALIDAR LOS DATOS
# ============================================================

# Formatear el nombre con la primera letra en mayúscula
nombre_formateado = nombre.title()
apellido_formateado = apellido.title()
nombre_completo = f"{nombre_formateado} {apellido_formateado}"

# Formatear la profesión
profesion_formateada = profesion.title()

# Calcular algunas estadísticas divertidas
dias_vividos = edad * 365
meses_vividos = edad * 12

# Determinar una descripción según la edad
if edad < 18:
    etapa = "¡Eres joven, el futuro es tuyo!"
elif edad < 30:
    etapa = "En tus mejores años de aprendizaje"
elif edad < 50:
    etapa = "Con experiencia y mucho por lograr"
else:
    etapa = "La sabiduría viene con los años"

# ============================================================
# PASO 3: GENERAR LA TARJETA
# ============================================================

# Calculamos el ancho de la tarjeta
ancho = 50

print()
print()

# Tarjeta principal
print("┌" + "─" * ancho + "┐")
print("│" + " " * ancho + "│")

# Nombre centrado
linea_nombre = f"  ★  {nombre_completo}  ★  "
print("│" + linea_nombre.center(ancho) + "│")

# Profesión
linea_profesion = profesion_formateada
print("│" + linea_profesion.center(ancho) + "│")

print("│" + " " * ancho + "│")
print("│" + "─" * ancho + "│")
print("│" + " " * ancho + "│")

# Datos personales
print("│" + f"  📍 {ciudad}, {pais}".ljust(ancho) + "│")
print("│" + f"  📧 {email}".ljust(ancho) + "│")
print("│" + f"  🎂 {edad} años  ({etapa})".ljust(ancho) + "│")

print("│" + " " * ancho + "│")
print("│" + "─" * ancho + "│")
print("│" + " " * ancho + "│")

# Habilidades
print("│" + "  🚀 HABILIDADES:".ljust(ancho) + "│")
print("│" + f"     • {habilidad1}".ljust(ancho) + "│")
print("│" + f"     • {habilidad2}".ljust(ancho) + "│")

print("│" + " " * ancho + "│")
print("│" + "─" * ancho + "│")
print("│" + " " * ancho + "│")

# Frase personal
print("│" + "  💬 Mi frase:".ljust(ancho) + "│")

# Si la frase es muy larga, la dividimos
if len(frase) <= ancho - 5:
    print("│" + f"  \"{frase}\"".ljust(ancho) + "│")
else:
    # Partimos la frase en dos líneas
    mitad = len(frase) // 2
    print("│" + f"  \"{frase[:mitad]}".ljust(ancho) + "│")
    print("│" + f"   {frase[mitad:]}\"".ljust(ancho) + "│")

print("│" + " " * ancho + "│")
print("└" + "─" * ancho + "┘")

# ============================================================
# ESTADÍSTICAS EXTRA
# ============================================================

print()
print("📊 DATOS CURIOSOS SOBRE TI:")
print(f"   • Has vivido aproximadamente {dias_vividos:,} días")
print(f"   • Eso son {meses_vividos} meses de experiencia de vida")
print(f"   • Tu nombre tiene {len(nombre_completo)} letras")
print(f"   • Tus iniciales son: {nombre[0].upper()}.{apellido[0].upper()}.")

# ============================================================
# MENSAJE DE CIERRE
# ============================================================

print()
print("╔══════════════════════════════════════════════╗")
print("║                                              ║")
print("║   🎉 ¡FELICITACIONES, {}! 🎉".format(nombre_formateado).center(46) + "║")
print("║                                              ║")
print("║   Completaste la FASE 1 del curso.           ║")
print("║                                              ║")
print("║   Lo que aprendiste:                         ║")
print("║   ✅ print() — mostrar información           ║")
print("║   ✅ Variables — guardar datos               ║")
print("║   ✅ input() — pedir datos al usuario        ║")
print("║   ✅ Strings — manipular texto               ║")
print("║   ✅ f-strings — combinar texto y variables  ║")
print("║                                              ║")
print("║   La Fase 2 te espera:                       ║")
print("║   🔵 Control de Flujo                        ║")
print("║   → if/elif/else, while, for, listas         ║")
print("║                                              ║")
print("╚══════════════════════════════════════════════╝")

# ============================================================
# 🎯 EJERCICIOS ADICIONALES
# ============================================================
#
# EJERCICIO 1: Personaliza el diseño
# ────────────────────────────────────
# Cambia los bordes de la tarjeta. En lugar de ─ y │,
# usa otros caracteres como = o * para crear un estilo diferente.
#
# EJERCICIO 2: Agregar más información
# ──────────────────────────────────────
# Agrega dos preguntas más al programa:
#   - ¿Cuál es tu red social favorita?
#   - ¿Cuál es tu hobby?
# Muestra esa información en la tarjeta.
#
# EJERCICIO 3: Tarjeta mínima
# ─────────────────────────────
# Crea una versión compacta de 3 líneas:
# ┌────────────────────────────┐
# │  Nombre - Profesión - País │
# └────────────────────────────┘
