# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 24: APIS — DATOS DE INTERNET                     ║
# ║  Fase 5: Archivos y Librerías                           ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es una API y para qué sirve
#    - Cómo instalar y usar la librería requests
#    - Hacer peticiones GET a APIs públicas
#    - Procesar respuestas JSON
#    - APIs públicas gratuitas para practicar
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. PRIMERO instala requests: pip install requests
#    2. Abre este archivo en VS Code
#    3. Haz clic en el botón ▶️ (arriba a la derecha)
#    4. ¡Necesitas conexión a internet para este ejercicio!
#
# ⏮️ ANTERIOR: dia23_pip_librerias.py
# ⏭️ SIGUIENTE: dia25_sqlite.py
# ════════════════════════════════════════════════════════════

import json

# Intentamos importar requests; si no está instalado, lo indicamos
try:
    import requests
    REQUESTS_DISPONIBLE = True
except ImportError:
    REQUESTS_DISPONIBLE = False
    print("⚠️  'requests' no está instalado.")
    print("   Para instalarlo, abre la terminal y escribe:")
    print("   pip install requests")
    print()
    print("   Mientras tanto, el código de demostración usará datos simulados.\n")

# ============================================================
# SECCIÓN 1: ¿QUÉ ES UNA API?
# ============================================================

# API = Application Programming Interface (Interfaz de Programación de Aplicaciones)
#
# Una API es como un "menú de restaurante" para datos:
# Tú pides algo específico (endpoint) y el servidor te da los datos.
#
# Ejemplo:
# - Tú: "Dame información del clima en Madrid"
# - API: { "ciudad": "Madrid", "temperatura": 22, "clima": "soleado" }
#
# La mayoría de las APIs usan HTTP (el mismo protocolo que los navegadores)
# y devuelven datos en formato JSON.
#
# Tipos de peticiones HTTP:
#   GET    → Obtener datos (como leer)
#   POST   → Enviar datos (como crear)
#   PUT    → Actualizar datos
#   DELETE → Eliminar datos
#
# Este archivo usa solo GET porque es lo más común y simple.

# ============================================================
# SECCIÓN 2: PETICIONES BÁSICAS CON requests
# ============================================================

if REQUESTS_DISPONIBLE:
    print("="*55)
    print("PETICIONES BÁSICAS CON requests")
    print("="*55)

    # requests.get(url) hace una petición GET a una URL
    # jsonplaceholder.typicode.com es una API pública de prueba
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        respuesta = requests.get(url, timeout=5)

        print(f"\nURL: {url}")
        print(f"Código de estado: {respuesta.status_code}")  # 200 = éxito
        print(f"Tipo de contenido: {respuesta.headers.get('Content-Type', 'N/A')}")

        # Convertir la respuesta JSON a diccionario Python:
        datos = respuesta.json()
        print(f"\nDatos recibidos:")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")

    except requests.exceptions.ConnectionError:
        print("❌ Sin conexión a internet. Usando datos de demostración.")
        datos = {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
        print(f"Datos simulados: {datos}")
    except requests.exceptions.Timeout:
        print("❌ La petición tardó demasiado.")

# ============================================================
# SECCIÓN 3: API DE POSTS — JSONPlaceholder
# ============================================================

if REQUESTS_DISPONIBLE:
    print("\n" + "="*55)
    print("API PÚBLICA: JSONPlaceholder (posts)")
    print("="*55)

    try:
        # Obtener los primeros 5 posts
        respuesta = requests.get("https://jsonplaceholder.typicode.com/posts",
                                  params={"_limit": 5}, timeout=5)

        if respuesta.status_code == 200:
            posts = respuesta.json()
            print(f"\n{len(posts)} posts obtenidos de la API:")
            for post in posts:
                titulo_corto = post['title'][:45] + "..." if len(post['title']) > 45 else post['title']
                print(f"\n  📝 ID: {post['id']} | Usuario: {post['userId']}")
                print(f"     Título: {titulo_corto}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de red: {e}")

# ============================================================
# SECCIÓN 4: API DE USUARIOS — JSONPlaceholder
# ============================================================

if REQUESTS_DISPONIBLE:
    print("\n" + "="*55)
    print("API: Buscar usuario por ID")
    print("="*55)

    try:
        user_id = int(input("\n¿Qué ID de usuario quieres ver? (1-10): "))
        user_id = max(1, min(10, user_id))  # Limitar entre 1 y 10

        respuesta = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}",
                                  timeout=5)

        if respuesta.status_code == 200:
            usuario = respuesta.json()
            print(f"\n👤 Usuario #{usuario['id']}")
            print(f"   Nombre: {usuario['name']}")
            print(f"   Username: @{usuario['username']}")
            print(f"   Email: {usuario['email']}")
            print(f"   Ciudad: {usuario['address']['city']}")
            print(f"   Empresa: {usuario['company']['name']}")
        else:
            print(f"❌ Error {respuesta.status_code}")

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"❌ Error: {e}")

# ============================================================
# SECCIÓN 5: GUARDAR DATOS DE API EN JSON
# ============================================================

if REQUESTS_DISPONIBLE:
    print("\n" + "="*55)
    print("GUARDAR DATOS DE API EN ARCHIVO JSON")
    print("="*55)

    try:
        respuesta = requests.get("https://jsonplaceholder.typicode.com/users",
                                  timeout=5)

        if respuesta.status_code == 200:
            usuarios = respuesta.json()

            # Guardar en archivo:
            with open("usuarios_api.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=2)

            print(f"✅ {len(usuarios)} usuarios guardados en 'usuarios_api.json'")

            # Mostrar un resumen:
            print(f"\nResumen de usuarios:")
            for u in usuarios[:3]:
                print(f"  {u['id']}. {u['name']} — {u['email']}")
            print(f"  ... y {len(usuarios)-3} más")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de red: {e}")

# ============================================================
# SECCIÓN 6: DEMO SIN INTERNET — DATOS SIMULADOS
# ============================================================

if not REQUESTS_DISPONIBLE:
    print("="*55)
    print("DEMO: Procesando datos JSON (sin internet)")
    print("="*55)

    # Simulamos datos que vendría de una API:
    datos_simulados = [
        {"id": 1, "nombre": "Colombia", "capital": "Bogotá", "poblacion": 51000000},
        {"id": 2, "nombre": "México", "capital": "Ciudad de México", "poblacion": 130000000},
        {"id": 3, "nombre": "Argentina", "capital": "Buenos Aires", "poblacion": 45000000},
        {"id": 4, "nombre": "España", "capital": "Madrid", "poblacion": 47000000},
        {"id": 5, "nombre": "Perú", "capital": "Lima", "poblacion": 33000000},
    ]

    print("\n🌍 Países (datos simulados):")
    for pais in datos_simulados:
        print(f"  {pais['id']}. {pais['nombre']:<15} Capital: {pais['capital']:<25} "
              f"Población: {pais['poblacion']:,}")

    total = sum(p["poblacion"] for p in datos_simulados)
    print(f"\n  Población total: {total:,}")

    # Guardar en JSON:
    with open("paises_demo.json", "w", encoding="utf-8") as f:
        json.dump(datos_simulados, f, ensure_ascii=False, indent=2)
    print("✅ Archivo 'paises_demo.json' creado")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: 3 peticiones diferentes (requiere internet y requests)
# ────────────────────────────────────────────────────────────────────
# Haz peticiones a estas 3 URLs y muestra datos seleccionados:
#   https://jsonplaceholder.typicode.com/todos?_limit=3
#   https://jsonplaceholder.typicode.com/comments?_limit=3
#   https://jsonplaceholder.typicode.com/albums?_limit=3
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Guardar respuesta en JSON
# ──────────────────────────────────────
# Pide al usuario un número del 1 al 10.
# Descarga todos los posts de ese usuario:
#   https://jsonplaceholder.typicode.com/posts?userId=N
# Guarda los posts en un archivo llamado "posts_usuario_N.json"
# Muestra cuántos posts tiene ese usuario.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Buscar info de un país (requiere internet)
# ────────────────────────────────────────────────────────
# Pide al usuario el nombre de un país en inglés.
# Usa la API: https://restcountries.com/v3.1/name/{nombre}
# Muestra: nombre oficial, capital, población, continente, moneda.
#
# ESCRIBE TU CÓDIGO AQUÍ:
