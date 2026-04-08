# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 26: GESTOR DE TAREAS CON JSON                    ║
# ║  Fase 6: Proyectos Finales                              ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Aplicar JSON para persistencia de datos
#    - Gestión de tareas con prioridades
#    - Guardar y cargar datos entre sesiones
#    - Proyecto completo y funcional
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Las tareas se guardan en tareas.json
#
# ⏮️ ANTERIOR: ../Fase5_Archivos_y_Librerias/dia25_sqlite.py
# ⏭️ SIGUIENTE: dia27_web_scraping.py
# ════════════════════════════════════════════════════════════

import json
import os
import datetime

ARCHIVO_TAREAS = "tareas.json"

PRIORIDADES = {
    "alta": "🔴",
    "media": "🟡",
    "baja": "🟢"
}

# ============================================================
# FUNCIONES DE PERSISTENCIA
# ============================================================

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("⚠️  Error al leer tareas. Iniciando con lista vacía.")
    return []


def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


# ============================================================
# FUNCIONES DE GESTIÓN
# ============================================================

def agregar_tarea(tareas, titulo, descripcion="", prioridad="media", categoria="General"):
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = {
        "id": max([t["id"] for t in tareas], default=0) + 1,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad.lower(),
        "categoria": categoria,
        "completada": False,
        "fecha_creacion": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "fecha_completacion": None
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    icono = PRIORIDADES.get(prioridad.lower(), "⚪")
    print(f"✅ Tarea #{nueva_tarea['id']} agregada: {icono} {titulo}")


def completar_tarea(tareas, tarea_id):
    """Marca una tarea como completada."""
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            if tarea["completada"]:
                print(f"ℹ️  La tarea #{tarea_id} ya estaba completada")
            else:
                tarea["completada"] = True
                tarea["fecha_completacion"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                guardar_tareas(tareas)
                print(f"✅ Tarea #{tarea_id} '{tarea['titulo']}' completada 🎉")
            return
    print(f"❌ Tarea #{tarea_id} no encontrada")


def eliminar_tarea(tareas, tarea_id):
    """Elimina una tarea por ID."""
    for i, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            eliminada = tareas.pop(i)
            guardar_tareas(tareas)
            print(f"🗑️  Tarea #{tarea_id} '{eliminada['titulo']}' eliminada")
            return
    print(f"❌ Tarea #{tarea_id} no encontrada")


def mostrar_tareas(tareas, filtro="todas"):
    """Muestra las tareas según el filtro."""
    if filtro == "pendientes":
        lista = [t for t in tareas if not t["completada"]]
        titulo_filtro = "PENDIENTES"
    elif filtro == "completadas":
        lista = [t for t in tareas if t["completada"]]
        titulo_filtro = "COMPLETADAS"
    else:
        lista = tareas
        titulo_filtro = "TODAS"

    # Ordenar por prioridad (alta primero)
    orden_prioridad = {"alta": 0, "media": 1, "baja": 2}
    lista_ordenada = sorted(lista, key=lambda t: (
        t["completada"],
        orden_prioridad.get(t["prioridad"], 1)
    ))

    print(f"\n{'='*60}")
    print(f"  📋 TAREAS {titulo_filtro} ({len(lista_ordenada)} total)")
    print(f"{'='*60}")

    if not lista_ordenada:
        print("  (No hay tareas)")
        return

    for tarea in lista_ordenada:
        icono_prior = PRIORIDADES.get(tarea["prioridad"], "⚪")
        estado = "✅" if tarea["completada"] else "⬜"
        fecha = tarea.get("fecha_creacion", "")[:10]

        print(f"\n  {estado} #{tarea['id']:>3} {icono_prior} {tarea['titulo']}")
        if tarea["descripcion"]:
            print(f"      📝 {tarea['descripcion']}")
        print(f"      🏷️  {tarea['categoria']} | 📅 {fecha} | Prioridad: {tarea['prioridad']}")
        if tarea["completada"] and tarea.get("fecha_completacion"):
            print(f"      ✅ Completada: {tarea['fecha_completacion']}")

    print(f"{'='*60}")


def mostrar_estadisticas(tareas):
    """Muestra estadísticas de las tareas."""
    total = len(tareas)
    completadas = sum(1 for t in tareas if t["completada"])
    pendientes = total - completadas
    porcentaje = (completadas / total * 100) if total > 0 else 0

    print(f"\n📊 ESTADÍSTICAS:")
    print(f"  Total de tareas: {total}")
    print(f"  ✅ Completadas: {completadas}")
    print(f"  ⬜ Pendientes: {pendientes}")
    print(f"  📈 Progreso: {porcentaje:.0f}%")

    if total > 0:
        barra_len = 20
        completas_barra = int(porcentaje / 100 * barra_len)
        barra = "█" * completas_barra + "░" * (barra_len - completas_barra)
        print(f"  [{barra}] {porcentaje:.0f}%")

    # Por prioridad:
    for prioridad, icono in PRIORIDADES.items():
        n = sum(1 for t in tareas if t["prioridad"] == prioridad and not t["completada"])
        if n > 0:
            print(f"  {icono} Pendientes de prioridad {prioridad}: {n}")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    tareas = cargar_tareas()

    # Agregar tareas de ejemplo si está vacío:
    if not tareas:
        print("📋 Agregando tareas de ejemplo...")
        agregar_tarea(tareas, "Aprender Python", "Completar el curso de 30 días", "alta", "Estudio")
        agregar_tarea(tareas, "Hacer ejercicio", "30 minutos de cardio", "media", "Salud")
        agregar_tarea(tareas, "Leer un libro", "Al menos 20 páginas", "baja", "Personal")
        agregar_tarea(tareas, "Proyecto Python", "Terminar el proyecto final del curso", "alta", "Estudio")

    print("\n" + "╔" + "═"*48 + "╗")
    print("║" + "  ✅ GESTOR DE TAREAS  ".center(48) + "║")
    print("╚" + "═"*48 + "╝")

    while True:
        pendientes = sum(1 for t in tareas if not t["completada"])
        print(f"\n[{pendientes} tarea(s) pendiente(s)]")
        print("1. Ver todas las tareas")
        print("2. Ver pendientes")
        print("3. Ver completadas")
        print("4. Agregar tarea")
        print("5. Completar tarea")
        print("6. Eliminar tarea")
        print("7. Ver estadísticas")
        print("0. Salir")

        opcion = input("\n¿Qué deseas hacer? ").strip()

        if opcion == "1":
            mostrar_tareas(tareas, "todas")
        elif opcion == "2":
            mostrar_tareas(tareas, "pendientes")
        elif opcion == "3":
            mostrar_tareas(tareas, "completadas")
        elif opcion == "4":
            titulo = input("Título de la tarea: ").strip()
            if titulo:
                descripcion = input("Descripción (Enter para omitir): ").strip()
                print("Prioridad: alta / media / baja")
                prioridad = input("Prioridad [media]: ").strip().lower() or "media"
                if prioridad not in PRIORIDADES:
                    prioridad = "media"
                categoria = input("Categoría [General]: ").strip() or "General"
                agregar_tarea(tareas, titulo, descripcion, prioridad, categoria)
        elif opcion == "5":
            mostrar_tareas(tareas, "pendientes")
            try:
                tarea_id = int(input("ID de la tarea a completar: "))
                completar_tarea(tareas, tarea_id)
            except ValueError:
                print("❌ ID inválido")
        elif opcion == "6":
            mostrar_tareas(tareas, "todas")
            try:
                tarea_id = int(input("ID de la tarea a eliminar: "))
                confirmar = input(f"¿Seguro que quieres eliminar la tarea #{tarea_id}? (s/n): ")
                if confirmar.lower() == "s":
                    eliminar_tarea(tareas, tarea_id)
            except ValueError:
                print("❌ ID inválido")
        elif opcion == "7":
            mostrar_estadisticas(tareas)
        elif opcion == "0":
            print(f"\n👋 ¡Hasta pronto! Tienes {pendientes} tarea(s) pendiente(s).")
            break
        else:
            print("❌ Opción no válida")

    # Limpiar archivo al salir (opcional — comenta para mantener los datos)
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)


main()
