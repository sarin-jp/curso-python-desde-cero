# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 22: CSV Y JSON — FORMATOS DE DATOS               ║
# ║  Fase 5: Archivos y Librerías                           ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - CSV: archivos de valores separados por comas
#    - JSON: formato de datos usado en internet
#    - Escribir y leer CSV con el módulo csv
#    - Escribir y leer JSON con el módulo json
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Se crearán archivos .csv y .json en la carpeta
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Abre los archivos creados para ver el formato
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia21_archivos_texto.py
# ⏭️ SIGUIENTE: dia23_pip_librerias.py
# ════════════════════════════════════════════════════════════

import csv
import json
import os

# ============================================================
# SECCIÓN 1: ¿QUÉ ES CSV?
# ============================================================

# CSV = Comma Separated Values (Valores Separados por Comas)
# Es un formato simple para guardar tablas de datos.
# Se puede abrir en Excel o Google Sheets.
#
# Ejemplo de un archivo CSV:
# nombre,apellido,edad,ciudad
# Ana,García,25,Madrid
# Carlos,López,30,Buenos Aires

# ============================================================
# SECCIÓN 2: ESCRIBIR CSV
# ============================================================

print("--- CREANDO ARCHIVO CSV ---")

estudiantes = [
    {"nombre": "Ana", "apellido": "García", "edad": 20, "nota": 88},
    {"nombre": "Carlos", "apellido": "López", "edad": 22, "nota": 75},
    {"nombre": "Beatriz", "apellido": "Martín", "edad": 21, "nota": 92},
    {"nombre": "David", "apellido": "Sánchez", "edad": 23, "nota": 68},
    {"nombre": "Elena", "apellido": "Torres", "edad": 20, "nota": 95},
]

# Escribir CSV con DictWriter (usa diccionarios):
with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "apellido", "edad", "nota"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()          # Escribe la primera fila con los nombres de columnas
    escritor.writerows(estudiantes) # Escribe todos los estudiantes

print("✅ Archivo 'estudiantes.csv' creado")

# ============================================================
# SECCIÓN 3: LEER CSV
# ============================================================

print("\n--- LEYENDO ARCHIVO CSV ---")

with open("estudiantes.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)  # Lee como diccionarios

    print(f"{'Nombre':<12} {'Apellido':<12} {'Edad':>5} {'Nota':>6}")
    print("-"*38)

    notas = []
    for fila in lector:
        print(f"{fila['nombre']:<12} {fila['apellido']:<12} {fila['edad']:>5} {fila['nota']:>6}")
        notas.append(float(fila["nota"]))

print(f"\nPromedio del grupo: {sum(notas)/len(notas):.1f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")

# ============================================================
# SECCIÓN 4: ¿QUÉ ES JSON?
# ============================================================

# JSON = JavaScript Object Notation
# Es el formato más popular para intercambiar datos en internet.
# Las APIs web usan JSON para enviar y recibir datos.
#
# Parece un diccionario de Python:
# {
#   "nombre": "Ana",
#   "edad": 25,
#   "hobbies": ["leer", "programar"]
# }

# ============================================================
# SECCIÓN 5: ESCRIBIR JSON
# ============================================================

print("\n--- CREANDO ARCHIVO JSON ---")

contactos = [
    {
        "id": 1,
        "nombre": "Ana García",
        "telefono": "+34 612 345 678",
        "email": "ana@ejemplo.com",
        "grupos": ["amigos", "trabajo"]
    },
    {
        "id": 2,
        "nombre": "Carlos López",
        "telefono": "+54 11 2345 6789",
        "email": "carlos@ejemplo.com",
        "grupos": ["familia"]
    },
    {
        "id": 3,
        "nombre": "Beatriz Martín",
        "telefono": "+52 55 1234 5678",
        "email": "beatriz@ejemplo.com",
        "grupos": ["amigos", "universidad"]
    }
]

# json.dump() escribe en archivo (indent=2 lo hace legible)
with open("contactos.json", "w", encoding="utf-8") as archivo:
    json.dump(contactos, archivo, ensure_ascii=False, indent=2)

print("✅ Archivo 'contactos.json' creado")

# ============================================================
# SECCIÓN 6: LEER JSON
# ============================================================

print("\n--- LEYENDO ARCHIVO JSON ---")

with open("contactos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Convierte JSON a diccionarios de Python

print(f"Contactos cargados: {len(datos)}")
for contacto in datos:
    grupos = ", ".join(contacto["grupos"])
    print(f"\n  👤 {contacto['nombre']}")
    print(f"     📞 {contacto['telefono']}")
    print(f"     📧 {contacto['email']}")
    print(f"     🏷️  Grupos: {grupos}")

# ============================================================
# SECCIÓN 7: json.dumps() y json.loads() — SIN ARCHIVOS
# ============================================================

# A veces necesitas convertir entre Python y JSON sin archivos:
datos_python = {"nombre": "Ana", "edad": 25, "activa": True, "notas": [8, 9, 10]}

# Python → JSON (texto)
texto_json = json.dumps(datos_python, ensure_ascii=False)
print(f"\nPython a JSON: {texto_json}")
print(f"Tipo: {type(texto_json)}")

# JSON (texto) → Python
datos_recuperados = json.loads(texto_json)
print(f"\nJSON a Python: {datos_recuperados}")
print(f"Tipo: {type(datos_recuperados)}")
print(f"Nombre: {datos_recuperados['nombre']}")

# ============================================================
# LIMPIEZA
# ============================================================
for f in ["estudiantes.csv", "contactos.json"]:
    if os.path.exists(f):
        os.remove(f)

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Lista de productos en CSV
# ───────────────────────────────────────
# Crea un archivo productos.csv con columnas: codigo, nombre, precio, stock
# Agrega al menos 5 productos.
# Luego léelo y muestra el total de inventario (precio * stock de cada producto).
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Configuración en JSON
# ────────────────────────────────────
# Crea un archivo configuracion.json con datos de un juego:
# { "jugador": "...", "nivel": 1, "puntos": 0, "vidas": 3 }
# Léelo, simula ganar puntos (+100) y subir de nivel,
# y guarda los cambios de vuelta en el archivo.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Promedio de notas desde CSV
# ──────────────────────────────────────────
# Crea un CSV con nombres y notas de 5 estudiantes.
# Lee el CSV y calcula:
#   - Promedio de cada estudiante
#   - El estudiante con mayor promedio
#   - Cuántos aprobaron (promedio >= 60)
#
# ESCRIBE TU CÓDIGO AQUÍ:
