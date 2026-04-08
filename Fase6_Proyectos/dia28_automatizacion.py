# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 28: AUTOMATIZACIÓN DE ARCHIVOS                   ║
# ║  Fase 6: Proyectos Finales                              ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - os: operaciones con el sistema de archivos
#    - shutil: copiar, mover y eliminar archivos/carpetas
#    - Organizar archivos automáticamente por extensión
#    - Renombrado masivo de archivos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. El programa creará carpetas de prueba y las limpiará después
#
# ⏮️ ANTERIOR: dia27_web_scraping.py
# ⏭️ SIGUIENTE: dia29_dashboard.py
# ════════════════════════════════════════════════════════════

import os
import shutil
import datetime

# ============================================================
# SECCIÓN 1: OPERACIONES BÁSICAS CON os
# ============================================================

print("="*55)
print("OPERACIONES CON ARCHIVOS Y CARPETAS")
print("="*55)

# Crear carpeta de pruebas:
CARPETA_PRUEBA = "prueba_automatizacion"
os.makedirs(CARPETA_PRUEBA, exist_ok=True)  # exist_ok=True no falla si ya existe
print(f"\n✅ Carpeta '{CARPETA_PRUEBA}' creada")

# Crear archivos de prueba:
archivos_prueba = [
    ("foto_vacaciones.jpg", "imagen"),
    ("foto_cumple.jpg", "imagen"),
    ("documento_importante.pdf", "documento"),
    ("informe_ventas.pdf", "documento"),
    ("cancion_favorita.mp3", "musica"),
    ("otro_audio.mp3", "musica"),
    ("video_tutorial.mp4", "video"),
    ("notas.txt", "texto"),
    ("codigo.py", "codigo"),
    ("datos.csv", "datos"),
    ("config.json", "datos"),
]

print(f"\n📄 Creando {len(archivos_prueba)} archivos de prueba...")
for nombre, tipo in archivos_prueba:
    ruta = os.path.join(CARPETA_PRUEBA, nombre)
    with open(ruta, "w") as f:
        f.write(f"Archivo de prueba: {nombre} (tipo: {tipo})\n")

print(f"✅ Archivos creados")

# Listar los archivos:
print(f"\nArchivos en '{CARPETA_PRUEBA}':")
for archivo in sorted(os.listdir(CARPETA_PRUEBA)):
    ruta_completa = os.path.join(CARPETA_PRUEBA, archivo)
    tamaño = os.path.getsize(ruta_completa)
    print(f"  📄 {archivo} ({tamaño} bytes)")

# ============================================================
# SECCIÓN 2: ORGANIZADOR AUTOMÁTICO DE ARCHIVOS
# ============================================================

print("\n" + "="*55)
print("🗂️  ORGANIZADOR AUTOMÁTICO DE ARCHIVOS")
print("="*55)

# Diccionario: extensión → nombre de carpeta destino
CATEGORIAS = {
    ".jpg":  "Imágenes",
    ".jpeg": "Imágenes",
    ".png":  "Imágenes",
    ".gif":  "Imágenes",
    ".pdf":  "Documentos",
    ".doc":  "Documentos",
    ".docx": "Documentos",
    ".xlsx": "Documentos",
    ".mp3":  "Música",
    ".wav":  "Música",
    ".ogg":  "Música",
    ".mp4":  "Videos",
    ".avi":  "Videos",
    ".mov":  "Videos",
    ".txt":  "Textos",
    ".py":   "Código",
    ".js":   "Código",
    ".html": "Código",
    ".csv":  "Datos",
    ".json": "Datos",
    ".xml":  "Datos",
}


def organizar_carpeta(carpeta_origen):
    """
    Organiza los archivos de una carpeta en subcarpetas
    según su tipo/extensión.
    """
    if not os.path.exists(carpeta_origen):
        print(f"❌ La carpeta '{carpeta_origen}' no existe")
        return

    archivos_movidos = 0
    archivos_no_reconocidos = []

    for nombre_archivo in os.listdir(carpeta_origen):
        ruta_archivo = os.path.join(carpeta_origen, nombre_archivo)

        # Saltar si es una carpeta:
        if os.path.isdir(ruta_archivo):
            continue

        # Obtener la extensión:
        _, extension = os.path.splitext(nombre_archivo)
        extension = extension.lower()

        # Determinar la carpeta destino:
        if extension in CATEGORIAS:
            carpeta_destino = os.path.join(carpeta_origen, CATEGORIAS[extension])
        else:
            carpeta_destino = os.path.join(carpeta_origen, "Otros")
            archivos_no_reconocidos.append(nombre_archivo)

        # Crear la carpeta destino si no existe:
        os.makedirs(carpeta_destino, exist_ok=True)

        # Mover el archivo:
        destino_final = os.path.join(carpeta_destino, nombre_archivo)

        # Si ya existe un archivo con ese nombre en destino, agregamos número:
        if os.path.exists(destino_final):
            base, ext = os.path.splitext(nombre_archivo)
            contador = 1
            while os.path.exists(destino_final):
                nuevo_nombre = f"{base}_{contador}{ext}"
                destino_final = os.path.join(carpeta_destino, nuevo_nombre)
                contador += 1

        shutil.move(ruta_archivo, destino_final)
        print(f"  📦 '{nombre_archivo}' → {CATEGORIAS.get(extension, 'Otros')}/")
        archivos_movidos += 1

    print(f"\n✅ {archivos_movidos} archivos organizados")
    if archivos_no_reconocidos:
        print(f"❓ Sin categoría: {archivos_no_reconocidos}")

    # Mostrar estructura resultante:
    print(f"\n📁 Estructura de '{carpeta_origen}':")
    for item in sorted(os.listdir(carpeta_origen)):
        ruta_item = os.path.join(carpeta_origen, item)
        if os.path.isdir(ruta_item):
            n_archivos = len(os.listdir(ruta_item))
            print(f"  📁 {item}/ ({n_archivos} archivo(s))")


organizar_carpeta(CARPETA_PRUEBA)

# ============================================================
# SECCIÓN 3: RENOMBRADOR MASIVO
# ============================================================

print("\n" + "="*55)
print("✏️  RENOMBRADOR MASIVO DE ARCHIVOS")
print("="*55)

# Crear carpeta con archivos mal nombrados para el ejemplo:
CARPETA_RENOMBRAR = "archivos_para_renombrar"
os.makedirs(CARPETA_RENOMBRAR, exist_ok=True)

# Crear archivos de prueba:
for i in range(1, 6):
    with open(os.path.join(CARPETA_RENOMBRAR, f"img{i:04d}.jpg"), "w") as f:
        f.write(f"imagen {i}")


def renombrar_masivo(carpeta, prefijo="archivo", extension_filtro=None):
    """
    Renombra todos los archivos de una carpeta con un prefijo
    y numeración secuencial.
    """
    archivos = []
    for archivo in sorted(os.listdir(carpeta)):
        ruta = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta):
            if extension_filtro:
                _, ext = os.path.splitext(archivo)
                if ext.lower() != extension_filtro.lower():
                    continue
            archivos.append(archivo)

    print(f"\nRenombrando {len(archivos)} archivos en '{carpeta}':")
    for i, archivo_viejo in enumerate(archivos, 1):
        _, ext = os.path.splitext(archivo_viejo)
        archivo_nuevo = f"{prefijo}_{i:03d}{ext}"
        ruta_vieja = os.path.join(carpeta, archivo_viejo)
        ruta_nueva = os.path.join(carpeta, archivo_nuevo)
        os.rename(ruta_vieja, ruta_nueva)
        print(f"  '{archivo_viejo}' → '{archivo_nuevo}'")

    print(f"✅ {len(archivos)} archivos renombrados")


renombrar_masivo(CARPETA_RENOMBRAR, prefijo="foto_vacaciones", extension_filtro=".jpg")

# ============================================================
# SECCIÓN 4: INFORMACIÓN DE ARCHIVOS Y CARPETAS
# ============================================================

print("\n" + "="*55)
print("📊 INFORMACIÓN DEL DIRECTORIO ACTUAL")
print("="*55)


def analizar_directorio(ruta="."):
    """Analiza estadísticas de un directorio."""
    total_archivos = 0
    total_tamaño = 0
    por_extension = {}

    for raiz, carpetas, archivos in os.walk(ruta):
        # Ignorar carpetas ocultas y de prueba
        carpetas[:] = [c for c in carpetas if not c.startswith(".")]

        for archivo in archivos:
            ruta_archivo = os.path.join(raiz, archivo)
            try:
                tamaño = os.path.getsize(ruta_archivo)
                total_archivos += 1
                total_tamaño += tamaño

                _, ext = os.path.splitext(archivo)
                ext = ext.lower() or "(sin extensión)"
                if ext not in por_extension:
                    por_extension[ext] = {"cantidad": 0, "tamaño": 0}
                por_extension[ext]["cantidad"] += 1
                por_extension[ext]["tamaño"] += tamaño
            except (PermissionError, OSError):
                pass

    return total_archivos, total_tamaño, por_extension


total_arch, total_tam, por_ext = analizar_directorio(".")

print(f"\n  Archivos totales: {total_arch}")
print(f"  Tamaño total: {total_tam:,} bytes ({total_tam/1024:.1f} KB)")

if por_ext:
    print(f"\n  Tipos de archivo:")
    for ext, datos in sorted(por_ext.items(), key=lambda x: x[1]["cantidad"], reverse=True)[:8]:
        print(f"    {ext:<15} {datos['cantidad']:>3} archivos")

# ============================================================
# LIMPIEZA — eliminar carpetas de prueba
# ============================================================

print("\n" + "="*55)
print("🧹 Limpiando archivos de prueba...")
for carpeta in [CARPETA_PRUEBA, CARPETA_RENOMBRAR]:
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)
        print(f"  🗑️  '{carpeta}' eliminada")
print("✅ Limpieza completada")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Organizar tus descargas
# ──────────────────────────────────────
# Usa la función organizar_carpeta() para organizar
# una carpeta real de tu computadora (¡haz una copia de seguridad antes!).
# Modifica las CATEGORIAS para incluir tipos de archivo que uses.
#
# EJERCICIO 2: Buscador de archivos
# ───────────────────────────────────
# Crea una función buscar_archivos(carpeta, extension) que:
#   - Recorra todos los subdirectorios
#   - Encuentre todos los archivos con esa extensión
#   - Devuelva una lista con las rutas completas
#   - Muestre el tamaño de cada uno y el total
# Úsalo para buscar todos los .py en el curso.
#
# ESCRIBE TU CÓDIGO AQUÍ:
