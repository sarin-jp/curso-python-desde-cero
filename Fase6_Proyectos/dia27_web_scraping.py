# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 27: WEB SCRAPING Y APIs PÚBLICAS                 ║
# ║  Fase 6: Proyectos Finales                              ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Qué es el web scraping y sus límites éticos
#    - Consumir APIs públicas con requests
#    - Procesar y presentar datos de internet
#    - Guardar resultados en archivos locales
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Asegúrate de tener requests instalado: pip install requests
#    2. Necesitas conexión a internet
#    3. Haz clic en ▶️
#
# ⏮️ ANTERIOR: dia26_gestor_tareas.py
# ⏭️ SIGUIENTE: dia28_automatizacion.py
# ════════════════════════════════════════════════════════════

import json
import os
import datetime

try:
    import requests
    REQUESTS_DISPONIBLE = True
except ImportError:
    REQUESTS_DISPONIBLE = False

# ============================================================
# SECCIÓN 1: ÉTICA DEL WEB SCRAPING
# ============================================================

print("="*60)
print("🧭 ÉTICA DEL WEB SCRAPING")
print("="*60)
print("""
El web scraping es la técnica de extraer datos de sitios web.
Es poderoso pero debe usarse con responsabilidad:

  ✅ PERMITIDO:
     - Sitios que ofrecen APIs públicas
     - Datos marcados como de libre uso
     - Sitios propios o con permiso explícito
     - Respetar el archivo robots.txt de cada sitio

  ❌ PROHIBIDO / MAL VISTO:
     - Datos personales sin consentimiento
     - Sobrecargar servidores con muchas peticiones
     - Violar términos de servicio del sitio
     - Datos protegidos por copyright

  📌 BUENAS PRÁCTICAS:
     - Usar APIs oficiales cuando existen
     - Agregar pausas entre peticiones (time.sleep)
     - Identificarte con un User-Agent real
     - No almacenar datos sensibles innecesariamente

En este curso usamos solo APIs PÚBLICAS y GRATUITAS.
""")

# ============================================================
# SECCIÓN 2: API HTTPBIN — PROBAR PETICIONES
# ============================================================

if REQUESTS_DISPONIBLE:
    print("="*60)
    print("API httpbin.org — Prueba de peticiones HTTP")
    print("="*60)

    try:
        # httpbin.org es una API para probar peticiones HTTP
        respuesta = requests.get("https://httpbin.org/get",
                                  params={"curso": "python", "dia": "27"},
                                  timeout=5)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            print(f"\nURL completa: {datos.get('url', 'N/A')}")
            print(f"Parámetros enviados: {datos.get('args', {})}")
            print(f"Tu IP: {datos.get('origin', 'N/A')}")
            cabeceras = datos.get("headers", {})
            print(f"User-Agent: {cabeceras.get('User-Agent', 'N/A')[:60]}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Sin conexión: {e}")

# ============================================================
# SECCIÓN 3: API JSONPLACEHOLDER — DATOS DE PRUEBA
# ============================================================

if REQUESTS_DISPONIBLE:
    print("\n" + "="*60)
    print("API JSONPlaceholder — Sistema de noticias simulado")
    print("="*60)

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def obtener_posts(limit=5):
        """Obtiene los últimos posts de la API."""
        try:
            resp = requests.get(f"{BASE_URL}/posts", params={"_limit": limit}, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException:
            return []

    def obtener_usuario(user_id):
        """Obtiene datos de un usuario por ID."""
        try:
            resp = requests.get(f"{BASE_URL}/users/{user_id}", timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException:
            return None

    def obtener_comentarios_post(post_id):
        """Obtiene comentarios de un post."""
        try:
            resp = requests.get(f"{BASE_URL}/comments", params={"postId": post_id}, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException:
            return []

    # Obtener y mostrar posts:
    posts = obtener_posts(5)
    if posts:
        print(f"\n📰 Últimas {len(posts)} noticias:")
        for post in posts:
            usuario = obtener_usuario(post["userId"])
            autor = usuario["name"] if usuario else f"Usuario {post['userId']}"
            titulo = post["title"][:50] + "..." if len(post["title"]) > 50 else post["title"]
            print(f"\n  📄 [{post['id']}] {titulo}")
            print(f"       Autor: {autor}")

        # Mostrar detalles del primer post:
        primer_post = posts[0]
        comentarios = obtener_comentarios_post(primer_post["id"])
        print(f"\n💬 El post #{primer_post['id']} tiene {len(comentarios)} comentarios")
        if comentarios:
            print(f"   Primer comentario de: {comentarios[0]['email']}")

# ============================================================
# SECCIÓN 4: GUARDAR DATOS EN ARCHIVO
# ============================================================

if REQUESTS_DISPONIBLE:
    print("\n" + "="*60)
    print("GUARDANDO DATOS DE LA API")
    print("="*60)

    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        if resp.status_code == 200:
            usuarios = resp.json()
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"datos_usuarios_{timestamp}.json"

            with open(nombre_archivo, "w", encoding="utf-8") as f:
                json.dump({
                    "fecha_descarga": datetime.datetime.now().isoformat(),
                    "fuente": "jsonplaceholder.typicode.com",
                    "total": len(usuarios),
                    "usuarios": usuarios
                }, f, ensure_ascii=False, indent=2)

            print(f"✅ {len(usuarios)} usuarios guardados en '{nombre_archivo}'")

            # Limpiar:
            if os.path.exists(nombre_archivo):
                os.remove(nombre_archivo)
                print(f"🗑️  Archivo temporal eliminado")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de red: {e}")

# ============================================================
# SECCIÓN 5: DEMO SIN INTERNET
# ============================================================

if not REQUESTS_DISPONIBLE:
    print("\n" + "="*60)
    print("DEMO: Procesando datos (sin internet / sin requests)")
    print("="*60)

    noticias_demo = [
        {"id": 1, "titulo": "Python 3.12 mejora su rendimiento", "autor": "TechNews", "likes": 245},
        {"id": 2, "titulo": "La IA sigue avanzando en 2024", "autor": "AIDaily", "likes": 189},
        {"id": 3, "titulo": "Open Source gana más adeptos", "autor": "DevWorld", "likes": 312},
    ]

    print("\n📰 Noticias simuladas:")
    for noticia in noticias_demo:
        print(f"\n  [{noticia['id']}] {noticia['titulo']}")
        print(f"       Autor: {noticia['autor']} | 👍 {noticia['likes']}")

    print("\n  Para usar APIs reales, instala requests:")
    print("  pip install requests")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: 3 endpoints diferentes
# ──────────────────────────────────────
# Usa JSONPlaceholder para obtener y mostrar datos de:
#   - /albums (álbumes)
#   - /photos?albumId=1 (fotos del álbum 1)
#   - /todos?userId=1 (tareas del usuario 1)
# Muestra 3 items de cada endpoint con sus datos principales.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Guardar en JSON con metadatos
# ───────────────────────────────────────────
# Descarga los 10 primeros posts de la API.
# Guárdalos en un archivo "mis_posts.json" que incluya:
#   - fecha de descarga
#   - URL fuente
#   - total de posts
#   - la lista de posts
# Lee el archivo y muestra el resumen.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Buscar información de país
# ─────────────────────────────────────────
# Usa la API: https://restcountries.com/v3.1/name/{pais}
# Pide al usuario el nombre de un país en inglés.
# Muestra: nombre oficial, capital, población, continente,
#          monedas y idiomas.
#
# ESCRIBE TU CÓDIGO AQUÍ:
