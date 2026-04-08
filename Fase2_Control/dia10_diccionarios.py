# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 10: DICCIONARIOS Y TUPLAS                        ║
# ║  Fase 2: Control de Flujo                               ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Diccionarios: datos con nombre (clave:valor)
#    - Acceder, agregar, modificar y eliminar entradas
#    - Recorrer diccionarios
#    - Tuplas: listas que no cambian
#    - PROYECTO: Agenda de contactos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Agrega tus propios datos al diccionario
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia09_listas.py
# ⏭️ SIGUIENTE: ../Fase3_Funciones/dia11_funciones.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UN DICCIONARIO?
# ============================================================

# Un diccionario guarda datos con NOMBRE (clave) y VALOR.
# Es como una agenda real: buscas por nombre y encuentras el teléfono.
# Se escribe con llaves {}

# Comparación con lista:
# Lista:       [25, "María", "Buenos Aires"]  ← ¿cuál es cuál?
# Diccionario: {"edad": 25, "nombre": "María", "ciudad": "Buenos Aires"}  ← todo claro

persona = {
    "nombre": "María",
    "apellido": "García",
    "edad": 28,
    "ciudad": "Madrid",
    "email": "maria@ejemplo.com",
    "es_programadora": True
}

print("Diccionario completo:", persona)

# ============================================================
# SECCIÓN 2: ACCEDER A VALORES
# ============================================================

# Acceder por clave (como índice, pero con nombre):
print(f"\nNombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Ciudad: {persona['ciudad']}")

# .get() → más seguro: devuelve None si la clave no existe
print(f"Email: {persona.get('email')}")
print(f"Teléfono: {persona.get('telefono', 'No registrado')}")  # Valor por defecto

# ============================================================
# SECCIÓN 3: MODIFICAR DICCIONARIOS
# ============================================================

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}
print(f"\nInventario original: {inventario}")

# Agregar nueva clave:
inventario["mangos"] = 12
print(f"Después de agregar mangos: {inventario}")

# Modificar un valor:
inventario["manzanas"] = 15  # Antes había 10, ahora 15
print(f"Después de modificar manzanas: {inventario}")

# Eliminar una clave:
del inventario["peras"]
print(f"Después de eliminar peras: {inventario}")

# .pop(clave) → elimina y devuelve el valor
cantidad_naranjas = inventario.pop("naranjas")
print(f"Eliminé las naranjas (había {cantidad_naranjas}): {inventario}")

# ============================================================
# SECCIÓN 4: RECORRER DICCIONARIOS
# ============================================================

calificaciones = {"Matemáticas": 85, "Historia": 92, "Física": 78, "Inglés": 96}

# Recorrer solo claves:
print("\nMaterias:")
for materia in calificaciones.keys():
    print(f"  - {materia}")

# Recorrer solo valores:
print("\nCalificaciones:")
for nota in calificaciones.values():
    print(f"  - {nota}")

# Recorrer AMBOS (lo más útil):
print("\nMaterias y calificaciones:")
for materia, nota in calificaciones.items():
    estado = "✅" if nota >= 70 else "❌"
    print(f"  {estado} {materia}: {nota}")

# ============================================================
# SECCIÓN 5: TUPLAS — LISTAS INMUTABLES
# ============================================================

# Una tupla es como una lista pero NO SE PUEDE MODIFICAR.
# Se usa () en lugar de []
# Útil para datos que nunca deben cambiar.

coordenadas = (40.4168, -3.7038)  # Latitud y longitud de Madrid
colores_rgb = (255, 128, 0)       # Naranja en RGB
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

print(f"\nCoordenadas de Madrid: {coordenadas}")
print(f"Color naranja (RGB): {colores_rgb}")
print(f"Primer día: {dias_semana[0]}")
print(f"Último día: {dias_semana[-1]}")

# También puedes recorrer tuplas con for:
print("\nDías de la semana:")
for i, dia in enumerate(dias_semana, 1):
    print(f"  {i}. {dia}")

# ============================================================
# SECCIÓN 6: PROYECTO — AGENDA DE CONTACTOS
# ============================================================

print("\n" + "="*50)
print("📱 AGENDA DE CONTACTOS")
print("="*50)

# La agenda es un diccionario donde cada clave es el nombre
# y el valor es otro diccionario con los datos del contacto
agenda = {}

while True:
    print("\nOpciones:")
    print("  1. Agregar contacto")
    print("  2. Buscar contacto")
    print("  3. Ver todos los contactos")
    print("  4. Eliminar contacto")
    print("  5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip().lower()
        agenda[nombre] = {"telefono": telefono, "email": email}
        print(f"✅ Contacto '{nombre}' agregado")

    elif opcion == "2":
        nombre = input("¿A quién buscas? ").strip().title()
        if nombre in agenda:
            contacto = agenda[nombre]
            print(f"\n📋 Datos de {nombre}:")
            print(f"   📞 Teléfono: {contacto['telefono']}")
            print(f"   📧 Email: {contacto['email']}")
        else:
            print(f"❌ '{nombre}' no está en la agenda")

    elif opcion == "3":
        if agenda:
            print(f"\n📋 Tienes {len(agenda)} contactos:")
            for nombre, datos in agenda.items():
                print(f"  👤 {nombre} — Tel: {datos['telefono']}")
        else:
            print("📭 La agenda está vacía")

    elif opcion == "4":
        nombre = input("¿Quién quieres eliminar? ").strip().title()
        if nombre in agenda:
            del agenda[nombre]
            print(f"✅ '{nombre}' eliminado")
        else:
            print(f"❌ '{nombre}' no encontrado")

    elif opcion == "5":
        print(f"\n👋 Cerrando agenda con {len(agenda)} contactos.")
        print("\n🎉 ¡FELICITACIONES! Completaste la FASE 2: Control de Flujo")
        print("   En la Fase 3 aprenderás a organizar tu código con funciones.")
        break

    else:
        print("❌ Opción no válida")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Inventario de tienda
# ──────────────────────────────────
# Crea un diccionario con 5 productos y sus precios.
# Muestra el producto más caro y el más barato.
# PISTA: puedes usar max(dict, key=dict.get)
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Contar palabras
# ─────────────────────────────
# Pide una frase al usuario.
# Crea un diccionario que cuente cuántas veces aparece cada letra.
# Muestra las 3 letras más frecuentes.
# PISTA: itera cada letra de la frase
#        si la letra está en el diccionario, suma 1
#        si no está, agrégala con valor 1
#
# ESCRIBE TU CÓDIGO AQUÍ:
