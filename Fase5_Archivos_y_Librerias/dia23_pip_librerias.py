# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 23: PIP Y LIBRERÍAS EXTERNAS                     ║
# ║  Fase 5: Archivos y Librerías                           ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es pip y cómo instalar librerías externas
#    - Módulo os: trabajar con el sistema operativo
#    - collections.Counter: contar elementos fácilmente
#    - sys: información del sistema
#    - Cómo encontrar e instalar librerías nuevas
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con los módulos
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia22_csv_json.py
# ⏭️ SIGUIENTE: dia24_apis.py
# ════════════════════════════════════════════════════════════

import os
import sys
from collections import Counter
import platform

# ============================================================
# SECCIÓN 1: ¿QUÉ ES PIP?
# ============================================================

# pip es el "gestor de paquetes" de Python.
# Es como una tienda de aplicaciones, pero para código Python.
# Con pip puedes instalar librerías que otros programadores crearon.
#
# CÓMO USAR PIP (en la terminal, NO en el código):
#
#   pip install nombre_libreria    → instala una librería
#   pip uninstall nombre_libreria  → desinstala
#   pip list                       → lista librerías instaladas
#   pip show nombre_libreria       → info sobre una librería
#   pip install libreria==1.2.3    → instala versión específica
#
# LIBRERÍAS POPULARES:
#   requests       → hacer peticiones HTTP (internet)
#   pandas         → análisis de datos
#   numpy          → matemáticas avanzadas
#   matplotlib     → gráficas y visualizaciones
#   flask          → crear sitios web
#   pillow         → manipular imágenes
#   colorama       → colores en la terminal

# ============================================================
# SECCIÓN 2: MÓDULO os — SISTEMA OPERATIVO
# ============================================================

print("="*50)
print("MÓDULO os — Sistema Operativo")
print("="*50)

# Directorio de trabajo actual:
directorio_actual = os.getcwd()
print(f"\nDirectorio actual: {directorio_actual}")

# Listar archivos en el directorio actual:
print(f"\nArchivos en el directorio actual:")
archivos = os.listdir(".")
for archivo in sorted(archivos)[:10]:  # Máximo 10
    if os.path.isfile(archivo):
        tamaño = os.path.getsize(archivo)
        print(f"  📄 {archivo} ({tamaño} bytes)")
    elif os.path.isdir(archivo):
        print(f"  📁 {archivo}/")

# Información sobre archivos:
print(f"\nInformación del sistema:")
print(f"  Sistema operativo: {platform.system()}")
print(f"  Versión: {platform.version()[:30]}...")
print(f"  Procesador: {platform.processor() or 'No disponible'}")

# Separador de rutas (\ en Windows, / en Mac/Linux):
print(f"\nSeparador de rutas: '{os.sep}'")
print(f"Separador de PATH: '{os.pathsep}'")

# Construir rutas de forma segura:
# os.path.join funciona en Windows y Mac/Linux
ruta = os.path.join("Fase5_Archivos_y_Librerias", "dia23_pip_librerias.py")
print(f"\nRuta construida con os.path.join: {ruta}")
print(f"¿Existe ese archivo? {os.path.exists(ruta)}")

# Variables de entorno:
usuario = os.environ.get("USER") or os.environ.get("USERNAME", "desconocido")
print(f"\nUsuario del sistema: {usuario}")

# Crear y eliminar directorios:
carpeta_test = "carpeta_de_prueba"
if not os.path.exists(carpeta_test):
    os.makedirs(carpeta_test)
    print(f"\n✅ Carpeta '{carpeta_test}' creada")

if os.path.exists(carpeta_test):
    os.rmdir(carpeta_test)
    print(f"✅ Carpeta '{carpeta_test}' eliminada")

# ============================================================
# SECCIÓN 3: MÓDULO sys — INFORMACIÓN DE PYTHON
# ============================================================

print("\n" + "="*50)
print("MÓDULO sys — Sistema Python")
print("="*50)

print(f"\nVersión de Python: {sys.version}")
print(f"Versión simplificada: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Plataforma: {sys.platform}")
print(f"Ruta del ejecutable Python: {sys.executable}")

# sys.argv — argumentos de línea de comandos:
print(f"\nArgumentos del script: {sys.argv}")
print(f"Nombre del script: {sys.argv[0]}")

# ============================================================
# SECCIÓN 4: collections.Counter — CONTAR ELEMENTOS
# ============================================================

print("\n" + "="*50)
print("collections.Counter — Contar elementos")
print("="*50)

# Counter cuenta cuántas veces aparece cada elemento:

# Contar letras en un texto:
texto = "programacion en python es muy divertido y poderoso"
contador_letras = Counter(texto.replace(" ", ""))

print(f"\nTexto: '{texto}'")
print(f"\nLetras más comunes (top 5):")
for letra, cantidad in contador_letras.most_common(5):
    barra = "█" * cantidad
    print(f"  '{letra}': {cantidad} veces  {barra}")

# Contar palabras:
palabras = texto.split()
contador_palabras = Counter(palabras)
print(f"\nTotal de palabras: {len(palabras)}")
print(f"Palabras únicas: {len(contador_palabras)}")
print(f"Palabras más comunes: {contador_palabras.most_common(3)}")

# Contar elementos en una lista:
colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo", "amarillo", "azul"]
contador_colores = Counter(colores)
print(f"\nColores y frecuencias: {dict(contador_colores)}")
print(f"Color más común: {contador_colores.most_common(1)[0]}")

# Operaciones con Counter:
c1 = Counter(["a", "b", "a", "c", "a"])
c2 = Counter(["a", "b", "b", "d"])
print(f"\nCounter 1: {c1}")
print(f"Counter 2: {c2}")
print(f"Suma: {c1 + c2}")

# ============================================================
# SECCIÓN 5: EJEMPLO PRÁCTICO — ANÁLISIS DE TEXTO
# ============================================================

print("\n" + "="*50)
print("ANÁLISIS DE TEXTO")
print("="*50)

def analizar_texto(texto):
    """Analiza estadísticas de un texto."""
    palabras = texto.lower().split()
    letras = [c for c in texto.lower() if c.isalpha()]

    contador_pal = Counter(palabras)
    contador_let = Counter(letras)

    print(f"\nTexto analizado:")
    print(f"  Caracteres totales: {len(texto)}")
    print(f"  Palabras totales: {len(palabras)}")
    print(f"  Palabras únicas: {len(contador_pal)}")
    print(f"  Oraciones (aprox): {texto.count('.') + texto.count('!') + texto.count('?')}")
    print(f"\n  Top 3 palabras más frecuentes:")
    for palabra, n in contador_pal.most_common(3):
        print(f"    '{palabra}': {n} veces")
    print(f"\n  Top 3 letras más frecuentes:")
    for letra, n in contador_let.most_common(3):
        print(f"    '{letra}': {n} veces")

texto_ejemplo = ("Python es un lenguaje de programación muy poderoso. "
                 "Python es fácil de aprender. Con Python puedes hacer "
                 "muchas cosas: web, datos, inteligencia artificial y más.")
analizar_texto(texto_ejemplo)

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Explorar os y sys
# ───────────────────────────────
# Usa os para:
#   - Mostrar el directorio donde están los archivos del curso
#   - Contar cuántos archivos .py hay en la carpeta actual
#   - Mostrar el tamaño total en bytes de todos esos archivos
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Counter con letras
# ──────────────────────────────────
# Pide una frase al usuario.
# Usa Counter para contar las vocales (a, e, i, o, u).
# Muestra cuántas veces aparece cada vocal.
# Muestra cuál es la vocal más frecuente.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Instala colorama (opcional)
# ──────────────────────────────────────────
# En la terminal ejecuta: pip install colorama
# Luego úsala para imprimir texto de colores:
#   from colorama import Fore, Back, Style, init
#   init()
#   print(Fore.RED + "Este texto es rojo")
#   print(Fore.GREEN + "Este texto es verde")
#   print(Style.RESET_ALL + "Este texto es normal")
#
# ESCRIBE TU CÓDIGO AQUÍ (después de instalar colorama):
