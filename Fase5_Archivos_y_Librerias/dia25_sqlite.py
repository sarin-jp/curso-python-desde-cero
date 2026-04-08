# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 25: SQLITE — TU PROPIA BASE DE DATOS             ║
# ║  Fase 5: Archivos y Librerías                           ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es una base de datos y por qué usarla
#    - SQLite: base de datos que viene con Python
#    - CREATE TABLE: crear una tabla
#    - INSERT: insertar datos
#    - SELECT: buscar datos
#    - WHERE: filtrar resultados
#    - UPDATE y DELETE: modificar y eliminar
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Se creará un archivo contactos.db en la carpeta
#
# ⏮️ ANTERIOR: dia24_apis.py
# ⏭️ SIGUIENTE: ../Fase6_Proyectos/dia26_gestor_tareas.py
# ════════════════════════════════════════════════════════════

import sqlite3
import os

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UNA BASE DE DATOS?
# ============================================================

# Una base de datos es como un Excel muy poderoso.
# Guarda información en tablas (filas y columnas).
# Puedes buscar, filtrar, ordenar y modificar datos muy rápidamente.
#
# SQLite es especial porque:
# - Viene incluida con Python (no necesitas instalar nada)
# - Guarda todo en un solo archivo .db
# - Perfecta para aplicaciones pequeñas y medianas
#
# SQL (Structured Query Language) es el lenguaje para hablar con bases de datos.

# ============================================================
# SECCIÓN 2: CONECTAR A LA BASE DE DATOS
# ============================================================

# Crear/conectar a un archivo .db:
# Si el archivo no existe, lo crea automáticamente.
conexion = sqlite3.connect("contactos.db")

# cursor es el "cursor" que ejecuta los comandos SQL:
cursor = conexion.cursor()

print("✅ Conectado a la base de datos 'contactos.db'")

# ============================================================
# SECCIÓN 3: CREAR UNA TABLA
# ============================================================

# CREATE TABLE crea una tabla si no existe:
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT,
        telefono TEXT,
        email TEXT UNIQUE,
        ciudad TEXT,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# TIPOS DE DATOS EN SQLite:
# INTEGER → números enteros
# TEXT    → texto
# REAL    → decimales
# BLOB    → datos binarios

# Guardar los cambios:
conexion.commit()
print("✅ Tabla 'contactos' creada (o ya existía)")

# ============================================================
# SECCIÓN 4: INSERTAR DATOS
# ============================================================

def insertar_contacto(nombre, apellido, telefono, email, ciudad):
    """Inserta un nuevo contacto en la base de datos."""
    try:
        cursor.execute("""
            INSERT INTO contactos (nombre, apellido, telefono, email, ciudad)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellido, telefono, email, ciudad))
        # ↑ Los ? son marcadores de posición — NUNCA pongas variables directamente
        # para evitar vulnerabilidades (SQL injection)

        conexion.commit()
        print(f"✅ Contacto '{nombre} {apellido}' agregado (ID: {cursor.lastrowid})")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"❌ El email '{email}' ya está registrado")
        return None

# Insertar contactos de ejemplo:
print("\n--- Insertando contactos ---")
insertar_contacto("Ana", "García", "+34 612 345 678", "ana@gmail.com", "Madrid")
insertar_contacto("Carlos", "López", "+52 55 1234 5678", "carlos@hotmail.com", "Ciudad de México")
insertar_contacto("Beatriz", "Martín", "+54 11 9876 5432", "beatriz@yahoo.com", "Buenos Aires")
insertar_contacto("David", "Torres", "+57 315 678 9012", "david@gmail.com", "Bogotá")
insertar_contacto("Elena", "Sánchez", "+34 987 654 321", "elena@outlook.com", "Barcelona")

# ============================================================
# SECCIÓN 5: CONSULTAR DATOS (SELECT)
# ============================================================

print("\n--- Todos los contactos ---")

cursor.execute("SELECT * FROM contactos ORDER BY nombre")
todos = cursor.fetchall()  # Obtiene TODOS los resultados

# Mostrar resultados:
print(f"\n{'ID':>3} {'Nombre':<12} {'Apellido':<12} {'Ciudad':<18} {'Email'}")
print("-"*65)
for fila in todos:
    print(f"{fila[0]:>3} {fila[1]:<12} {fila[2]:<12} {fila[5]:<18} {fila[4]}")

# Contar registros:
cursor.execute("SELECT COUNT(*) FROM contactos")
total = cursor.fetchone()[0]
print(f"\nTotal de contactos: {total}")

# ============================================================
# SECCIÓN 6: BUSCAR CON WHERE
# ============================================================

print("\n--- Búsqueda por ciudad ---")
ciudad_buscar = "Madrid"

cursor.execute("SELECT nombre, apellido, email FROM contactos WHERE ciudad = ?",
               (ciudad_buscar,))
resultados = cursor.fetchall()

print(f"\nContactos en {ciudad_buscar}:")
for contacto in resultados:
    print(f"  {contacto[0]} {contacto[1]} — {contacto[2]}")

# Búsqueda parcial con LIKE:
print("\n--- Búsqueda por email con 'gmail' ---")
cursor.execute("SELECT nombre, apellido, email FROM contactos WHERE email LIKE ?",
               ("%gmail%",))
gmail_users = cursor.fetchall()
for u in gmail_users:
    print(f"  {u[0]} {u[1]} — {u[2]}")

# ============================================================
# SECCIÓN 7: ACTUALIZAR Y ELIMINAR
# ============================================================

print("\n--- Actualizar contacto ---")
cursor.execute("UPDATE contactos SET telefono = ? WHERE email = ?",
               ("+34 699 888 777", "ana@gmail.com"))
conexion.commit()
filas_afectadas = cursor.rowcount
print(f"✅ {filas_afectadas} contacto(s) actualizado(s)")

print("\n--- Eliminar contacto ---")
cursor.execute("DELETE FROM contactos WHERE email = ?", ("elena@outlook.com",))
conexion.commit()
print(f"✅ {cursor.rowcount} contacto(s) eliminado(s)")

# ============================================================
# SECCIÓN 8: MENÚ INTERACTIVO
# ============================================================

def mostrar_todos_db():
    cursor.execute("SELECT id, nombre, apellido, telefono, ciudad FROM contactos ORDER BY nombre")
    contactos_db = cursor.fetchall()
    if contactos_db:
        print(f"\n{'ID':>3} {'Nombre':<15} {'Apellido':<15} {'Teléfono':<20} {'Ciudad'}")
        print("-"*65)
        for c in contactos_db:
            print(f"{c[0]:>3} {c[1]:<15} {c[2]:<15} {c[3]:<20} {c[4]}")
    else:
        print("📭 No hay contactos")


print("\n" + "="*50)
print("📱 AGENDA CON BASE DE DATOS SQLITE")
print("="*50)

while True:
    print("\nOpciones:")
    print("  1. Ver todos los contactos")
    print("  2. Agregar contacto")
    print("  3. Buscar contacto")
    print("  4. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        mostrar_todos_db()

    elif opcion == "2":
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip().lower()
        ciudad = input("Ciudad: ").strip()
        insertar_contacto(nombre, apellido, telefono, email, ciudad)

    elif opcion == "3":
        termino = input("Buscar por nombre o ciudad: ").strip()
        cursor.execute("""
            SELECT nombre, apellido, telefono, email, ciudad FROM contactos
            WHERE nombre LIKE ? OR ciudad LIKE ?
            ORDER BY nombre
        """, (f"%{termino}%", f"%{termino}%"))
        encontrados = cursor.fetchall()
        if encontrados:
            print(f"\n{len(encontrados)} resultado(s):")
            for c in encontrados:
                print(f"  {c[0]} {c[1]} | {c[2]} | {c[3]} | {c[4]}")
        else:
            print(f"❌ No se encontraron resultados para '{termino}'")

    elif opcion == "4":
        break

# Cerrar la conexión:
conexion.close()
print("\n✅ Conexión cerrada.")

# Limpiar archivo de prueba:
if os.path.exists("contactos.db"):
    os.remove("contactos.db")

print("\n" + "="*55)
print("🎉 ¡FELICITACIONES! Completaste la FASE 5")
print("   Archivos y Librerías")
print()
print("   Lo que aprendiste:")
print("   ✅ Archivos de texto (open, read, write)")
print("   ✅ CSV y JSON")
print("   ✅ pip y librerías externas")
print("   ✅ APIs y peticiones HTTP")
print("   ✅ SQLite y bases de datos")
print()
print("   La Fase 6 te espera: ¡Proyectos Finales!")
print("="*55)

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Actualizar y eliminar con menú
# ────────────────────────────────────────────
# Agrega al menú dos opciones:
#   - Actualizar el teléfono de un contacto (buscar por email)
#   - Eliminar un contacto (buscar por nombre)
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Menú interactivo completo
# ───────────────────────────────────────
# Extiende el menú actual para incluir:
#   - Ordenar por nombre, ciudad o fecha
#   - Ver solo contactos de una ciudad específica
#   - Contar cuántos contactos hay por ciudad
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Tabla de categorías
# ─────────────────────────────────
# Crea una segunda tabla "categorias" con: id, nombre
# Agrega datos: Amigos, Trabajo, Familia, Universidad
# Modifica la tabla contactos para tener una columna categoria_id
# Haz un JOIN para mostrar el nombre de la categoría junto al contacto.
# PISTA: SELECT c.nombre, cat.nombre FROM contactos c
#        JOIN categorias cat ON c.categoria_id = cat.id
#
# ESCRIBE TU CÓDIGO AQUÍ:
