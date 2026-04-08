# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 21: ARCHIVOS DE TEXTO — LEER Y ESCRIBIR          ║
# ║  Fase 5: Archivos y Librerías                           ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Cómo crear, leer y escribir archivos de texto
#    - open() con diferentes modos: r, w, a
#    - El bloque "with" para manejar archivos de forma segura
#    - PROYECTO: Diario personal en archivo de texto
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. El programa creará archivos en la misma carpeta
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Abre los archivos .txt creados para verificar
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: ../Fase4_POO/dia20_proyecto_banco.py
# ⏭️ SIGUIENTE: dia22_csv_json.py
# ════════════════════════════════════════════════════════════

import os
import datetime

# ============================================================
# SECCIÓN 1: MODOS DE APERTURA DE ARCHIVOS
# ============================================================

# open(nombre_archivo, modo) abre un archivo.
# Modos:
#   "r"  → leer (read): el archivo debe existir
#   "w"  → escribir (write): SOBREESCRIBE si existe, crea si no existe
#   "a"  → añadir (append): agrega al final sin borrar lo anterior
#   "r+" → leer y escribir
#   "rb" → leer en binario (para imágenes, etc.)

# ¡SIEMPRE usa "with"! Se encarga de cerrar el archivo automáticamente.

# ============================================================
# SECCIÓN 2: ESCRIBIR EN UN ARCHIVO
# ============================================================

print("--- ESCRIBIR EN ARCHIVO ---")

# Crear y escribir un archivo:
with open("mi_primer_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("¡Hola! Esto es mi primer archivo de texto.\n")
    archivo.write("Python puede leer y escribir archivos.\n")
    archivo.write("Esto es muy útil para guardar datos.\n")

print("✅ Archivo 'mi_primer_archivo.txt' creado")

# Escribir múltiples líneas con writelines():
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n", "Línea 4\n"]
with open("multiples_lineas.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
print("✅ Archivo 'multiples_lineas.txt' creado")

# ============================================================
# SECCIÓN 3: LEER UN ARCHIVO
# ============================================================

print("\n--- LEER ARCHIVO ---")

# Leer todo el contenido de una vez:
with open("mi_primer_archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("Contenido completo:")
    print(contenido)

# Leer línea por línea (mejor para archivos grandes):
print("Leyendo línea por línea:")
with open("mi_primer_archivo.txt", "r", encoding="utf-8") as archivo:
    for numero, linea in enumerate(archivo, 1):
        print(f"  Línea {numero}: {linea.strip()}")

# Leer todas las líneas como lista:
with open("mi_primer_archivo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(f"\nTotal de líneas: {len(lineas)}")

# ============================================================
# SECCIÓN 4: AÑADIR AL FINAL (append)
# ============================================================

print("\n--- AÑADIR CONTENIDO ---")

# Añadir sin borrar lo existente:
with open("mi_primer_archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea fue agregada después.\n")
    archivo.write(f"Fecha de modificación: {datetime.date.today()}\n")

print("✅ Contenido añadido")

# Verificar el resultado:
with open("mi_primer_archivo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())

# ============================================================
# SECCIÓN 5: VERIFICAR SI UN ARCHIVO EXISTE
# ============================================================

print("--- VERIFICAR ARCHIVOS ---")
archivos_a_verificar = ["mi_primer_archivo.txt", "archivo_inexistente.txt"]

for nombre in archivos_a_verificar:
    if os.path.exists(nombre):
        tamaño = os.path.getsize(nombre)
        print(f"✅ '{nombre}' existe ({tamaño} bytes)")
    else:
        print(f"❌ '{nombre}' no existe")

# ============================================================
# SECCIÓN 6: PROYECTO — DIARIO PERSONAL
# ============================================================

NOMBRE_DIARIO = "mi_diario.txt"

def escribir_entrada():
    """Escribe una nueva entrada en el diario."""
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    print("\nEscribe tu entrada (escribe 'FIN' en una línea para terminar):")

    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)

    if lineas:
        with open(NOMBRE_DIARIO, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"📅 {fecha}\n")
            f.write(f"{'─'*50}\n")
            for linea in lineas:
                f.write(linea + "\n")
        print("✅ Entrada guardada en el diario")
    else:
        print("❌ No se escribió nada")


def leer_diario():
    """Lee todas las entradas del diario."""
    if not os.path.exists(NOMBRE_DIARIO):
        print("📖 El diario está vacío. ¡Escribe tu primera entrada!")
        return

    with open(NOMBRE_DIARIO, "r", encoding="utf-8") as f:
        contenido = f.read()

    if contenido.strip():
        print(f"\n📖 Mi Diario Personal:")
        print(contenido)
    else:
        print("📖 El diario está vacío")


print("\n" + "="*45)
print("📔 DIARIO PERSONAL")
print("="*45)

while True:
    print("\nOpciones:")
    print("  1. Escribir nueva entrada")
    print("  2. Leer el diario")
    print("  3. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        escribir_entrada()
    elif opcion == "2":
        leer_diario()
    elif opcion == "3":
        print("👋 ¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida")

# ============================================================
# LIMPIEZA: Eliminar archivos de prueba
# ============================================================
for f in ["mi_primer_archivo.txt", "multiples_lineas.txt"]:
    if os.path.exists(f):
        os.remove(f)

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Contar palabras en un archivo
# ────────────────────────────────────────────
# Crea un archivo de texto con 3 párrafos (puedes copiarlo de algún sitio).
# Luego escribe código que:
#   - Cuente el número de líneas
#   - Cuente el número de palabras
#   - Cuente el número de caracteres
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Copiar un archivo
# ──────────────────────────────
# Escribe una función copiar_archivo(origen, destino) que:
#   - Lee el archivo origen
#   - Escribe su contenido en el archivo destino
#   - Muestra un mensaje de éxito
# No uses shutil, hazlo manualmente con open().
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Buscar una palabra en un archivo
# ───────────────────────────────────────────────
# Pide al usuario el nombre de un archivo y una palabra.
# Muestra en qué líneas aparece esa palabra.
# Muestra cuántas veces aparece en total.
#
# ESCRIBE TU CÓDIGO AQUÍ:
