# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 9: LISTAS — COLECCIONES DE DATOS                 ║
# ║  Fase 2: Control de Flujo                               ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es una lista y cómo crearla
#    - Acceder, agregar, eliminar y modificar elementos
#    - Métodos de lista: append, remove, sort, etc.
#    - Funciones: len, max, min, sum
#    - enumerate() para saber la posición mientras recorres
#    - PROYECTO: Lista de compras interactiva
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con las listas
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia08_for.py
# ⏭️ SIGUIENTE: dia10_diccionarios.py
# ════════════════════════════════════════════════════════════

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UNA LISTA?
# ============================================================

# Una lista guarda MÚLTIPLES valores en UNA sola variable.
# Se escribe con corchetes [] y los elementos separados por comas.
# Los elementos pueden ser de distintos tipos.

# Crear listas:
frutas = ["manzana", "naranja", "mango", "uva", "pera"]
numeros = [10, 25, 3, 87, 44, 2, 15]
mixta = ["Hola", 42, True, 3.14, "Python"]
vacia = []  # Lista vacía

print("Frutas:", frutas)
print("Números:", numeros)
print("Mixta:", mixta)

# ============================================================
# SECCIÓN 2: ACCEDER A ELEMENTOS
# ============================================================

# Se usa el índice entre corchetes (igual que con strings):
# El primer elemento es índice 0

print(f"\nPrimera fruta: {frutas[0]}")     # manzana
print(f"Tercera fruta: {frutas[2]}")       # mango
print(f"Última fruta: {frutas[-1]}")       # pera
print(f"Penúltima: {frutas[-2]}")          # uva

# Slicing en listas (igual que en strings):
print(f"\nPrimeras 3: {frutas[:3]}")
print(f"Últimas 2: {frutas[-2:]}")
print(f"Desde la 2 hasta la 4: {frutas[1:4]}")

# ============================================================
# SECCIÓN 3: MODIFICAR LISTAS
# ============================================================

colores = ["rojo", "verde", "azul"]
print(f"\nColores originales: {colores}")

# .append(elemento) → agrega AL FINAL
colores.append("amarillo")
print(f"Después de append: {colores}")

# .insert(posicion, elemento) → agrega en una posición específica
colores.insert(1, "naranja")  # Inserta "naranja" en posición 1
print(f"Después de insert: {colores}")

# Modificar un elemento:
colores[0] = "morado"  # Cambia "rojo" por "morado"
print(f"Después de modificar [0]: {colores}")

# .remove(elemento) → elimina la primera ocurrencia del elemento
colores.remove("verde")
print(f"Después de remove: {colores}")

# .pop(posicion) → elimina y devuelve el elemento en esa posición
eliminado = colores.pop(0)  # Elimina el primero
print(f"Eliminé: {eliminado}. Lista: {colores}")

# ============================================================
# SECCIÓN 4: MÉTODOS Y FUNCIONES ÚTILES
# ============================================================

notas = [85, 92, 78, 95, 88, 72, 96, 84]
print(f"\nNotas: {notas}")

# Funciones básicas:
print(f"Cantidad de notas: {len(notas)}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")
print(f"Suma de notas: {sum(notas)}")
print(f"Promedio: {sum(notas) / len(notas):.1f}")

# .sort() → ordena la lista (modifica la original)
notas_ordenadas = notas.copy()  # Hacemos una copia para no alterar el original
notas_ordenadas.sort()
print(f"Notas ordenadas: {notas_ordenadas}")

notas_ordenadas.sort(reverse=True)  # De mayor a menor
print(f"De mayor a menor: {notas_ordenadas}")

# sorted() → devuelve una nueva lista ordenada (no modifica la original)
nombres = ["Carlos", "Ana", "Beatriz", "David"]
nombres_ordenados = sorted(nombres)
print(f"\nNombres originales: {nombres}")
print(f"Nombres ordenados: {nombres_ordenados}")

# .count(elemento) → cuenta cuántas veces aparece algo
lista_repetida = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"\nEl 2 aparece {lista_repetida.count(2)} veces")

# in → verifica si un elemento está en la lista
if "Ana" in nombres:
    print("Ana está en la lista ✅")

# ============================================================
# SECCIÓN 5: enumerate() — POSICIÓN Y VALOR JUNTOS
# ============================================================

# enumerate() te da el índice Y el valor al mismo tiempo:
participantes = ["Sofía", "Miguel", "Laura", "Pedro"]
print("\nClasificación:")
for posicion, nombre in enumerate(participantes, start=1):
    print(f"  {posicion}° puesto: {nombre}")

# ============================================================
# SECCIÓN 6: PROYECTO — LISTA DE COMPRAS INTERACTIVA
# ============================================================

print("\n" + "="*45)
print("🛒 LISTA DE COMPRAS")
print("="*45)

lista_compras = []

while True:
    print(f"\nProductos en la lista: {len(lista_compras)}")
    if lista_compras:
        for i, producto in enumerate(lista_compras, 1):
            print(f"  {i}. {producto}")

    print("\nOpciones:")
    print("  a - Agregar producto")
    print("  e - Eliminar producto")
    print("  s - Salir")

    opcion = input("¿Qué deseas hacer? ").lower()

    if opcion == "a":
        producto = input("¿Qué producto quieres agregar? ").strip()
        if producto:
            lista_compras.append(producto.title())
            print(f"✅ '{producto.title()}' agregado")
        else:
            print("❌ Nombre vacío, no se agregó nada")

    elif opcion == "e":
        if lista_compras:
            producto = input("¿Qué producto quieres eliminar? ").strip()
            if producto.title() in lista_compras:
                lista_compras.remove(producto.title())
                print(f"✅ '{producto.title()}' eliminado")
            else:
                print(f"❌ '{producto}' no está en la lista")
        else:
            print("❌ La lista está vacía")

    elif opcion == "s":
        print(f"\n📋 Tu lista final tiene {len(lista_compras)} productos:")
        for i, producto in enumerate(lista_compras, 1):
            print(f"  {i}. {producto}")
        break
    else:
        print("❌ Opción no válida")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Mayor de 5 números
# ────────────────────────────────
# Crea una lista con 5 números pedidos al usuario.
# Muestra el mayor, el menor y el promedio.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Ordenar nombres
# ─────────────────────────────
# Pide al usuario 5 nombres (uno por uno con input).
# Guárdalos en una lista y muéstralos ordenados alfabéticamente.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Eliminar duplicados
# ─────────────────────────────────
# Dada esta lista: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Crea una nueva lista sin duplicados (cada número solo aparece una vez).
# Luego muestra cuántos números únicos hay.
# PISTA: puedes usar "if numero not in nueva_lista"
#
# ESCRIBE TU CÓDIGO AQUÍ:
