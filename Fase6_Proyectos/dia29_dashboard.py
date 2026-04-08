# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 29: DASHBOARD EN TERMINAL                        ║
# ║  Fase 6: Proyectos Finales                              ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Generar y analizar datos estadísticos
#    - Visualizar datos con barras en la terminal
#    - collections.Counter para análisis
#    - Calcular estadísticas descriptivas
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira el dashboard en la terminal
#
# ⏮️ ANTERIOR: dia28_automatizacion.py
# ⏭️ SIGUIENTE: dia30_proyecto_final.py
# ════════════════════════════════════════════════════════════

import random
import datetime
from collections import Counter

# ============================================================
# SECCIÓN 1: GENERACIÓN DE DATOS SIMULADOS
# ============================================================

# Datos de ventas de una tienda de tecnología
PRODUCTOS = ["Laptop", "Mouse", "Teclado", "Monitor", "Auriculares",
             "Webcam", "USB Hub", "Cable HDMI", "Mousepad", "Disco SSD"]
CATEGORIAS = ["Computadoras", "Periféricos", "Accesorios", "Almacenamiento"]
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# Generamos ventas simuladas para todo un año
random.seed(42)  # Seed fija para que los resultados sean reproducibles

ventas = []
for mes_num in range(1, 13):
    for _ in range(random.randint(40, 80)):  # 40-80 ventas por mes
        producto = random.choice(PRODUCTOS)
        precio = {
            "Laptop": random.uniform(600, 1200),
            "Mouse": random.uniform(15, 80),
            "Teclado": random.uniform(25, 120),
            "Monitor": random.uniform(200, 500),
            "Auriculares": random.uniform(30, 200),
            "Webcam": random.uniform(40, 150),
            "USB Hub": random.uniform(20, 60),
            "Cable HDMI": random.uniform(8, 25),
            "Mousepad": random.uniform(10, 40),
            "Disco SSD": random.uniform(60, 200),
        }.get(producto, 50)

        ventas.append({
            "mes": mes_num,
            "mes_nombre": MESES[mes_num - 1],
            "producto": producto,
            "precio": round(precio, 2),
            "cantidad": random.randint(1, 5)
        })

print(f"📊 Datos generados: {len(ventas)} transacciones en el año")

# ============================================================
# SECCIÓN 2: FUNCIONES DE VISUALIZACIÓN
# ============================================================

def barra_horizontal(valor, maximo, ancho=30, caracter="█"):
    """Crea una barra horizontal proporcional al valor."""
    if maximo == 0:
        return ""
    longitud = int((valor / maximo) * ancho)
    return caracter * longitud + "░" * (ancho - longitud)


def formatear_dinero(cantidad):
    """Formatea un número como dinero."""
    return f"${cantidad:>10,.2f}"


def titulo_seccion(titulo):
    """Muestra un título de sección."""
    print(f"\n{'═'*60}")
    print(f"  📊 {titulo.upper()}")
    print(f"{'═'*60}")

# ============================================================
# SECCIÓN 3: CÁLCULOS ESTADÍSTICOS
# ============================================================

# Ingresos totales por mes
ingresos_por_mes = {}
for mes_num, mes_nombre in enumerate(MESES, 1):
    ventas_mes = [v["precio"] * v["cantidad"] for v in ventas if v["mes"] == mes_num]
    ingresos_por_mes[mes_nombre] = sum(ventas_mes)

# Ventas por producto
ventas_por_producto = {}
for v in ventas:
    ingreso = v["precio"] * v["cantidad"]
    if v["producto"] not in ventas_por_producto:
        ventas_por_producto[v["producto"]] = {"ingresos": 0, "unidades": 0, "transacciones": 0}
    ventas_por_producto[v["producto"]]["ingresos"] += ingreso
    ventas_por_producto[v["producto"]]["unidades"] += v["cantidad"]
    ventas_por_producto[v["producto"]]["transacciones"] += 1

# Contador de transacciones por producto
contador_transacciones = Counter({p: d["transacciones"] for p, d in ventas_por_producto.items()})

# ============================================================
# SECCIÓN 4: DASHBOARD PRINCIPAL
# ============================================================

print("\n" + "╔" + "═"*58 + "╗")
print("║" + "  🏪 DASHBOARD DE VENTAS — TIENDA TECH 2024  ".center(58) + "║")
print("║" + f"  Generado: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}  ".ljust(58) + "║")
print("╚" + "═"*58 + "╝")

# ============================================================
# PANEL 1: RESUMEN EJECUTIVO
# ============================================================

titulo_seccion("RESUMEN EJECUTIVO")

ingreso_total = sum(ingresos_por_mes.values())
total_transacciones = len(ventas)
ticket_promedio = ingreso_total / total_transacciones if total_transacciones > 0 else 0
mes_mejor = max(ingresos_por_mes, key=ingresos_por_mes.get)
mes_peor = min(ingresos_por_mes, key=ingresos_por_mes.get)

print(f"\n  💰 Ingresos totales del año:  {formatear_dinero(ingreso_total)}")
print(f"  🛒 Total transacciones:          {total_transacciones:>10,}")
print(f"  🎯 Ticket promedio:          {formatear_dinero(ticket_promedio)}")
print(f"  📈 Mejor mes:                 {mes_mejor} ({formatear_dinero(ingresos_por_mes[mes_mejor])})")
print(f"  📉 Menor mes:                 {mes_peor} ({formatear_dinero(ingresos_por_mes[mes_peor])})")

# ============================================================
# PANEL 2: INGRESOS POR MES
# ============================================================

titulo_seccion("INGRESOS POR MES")

maximo_mes = max(ingresos_por_mes.values())
print()
for mes, ingreso in ingresos_por_mes.items():
    barra = barra_horizontal(ingreso, maximo_mes, ancho=25)
    print(f"  {mes} │{barra}│ {formatear_dinero(ingreso)}")

# ============================================================
# PANEL 3: TOP 5 PRODUCTOS POR INGRESOS
# ============================================================

titulo_seccion("TOP 5 PRODUCTOS POR INGRESOS")

productos_ordenados = sorted(ventas_por_producto.items(),
                              key=lambda x: x[1]["ingresos"], reverse=True)
maximo_producto = productos_ordenados[0][1]["ingresos"]

print()
for i, (producto, datos) in enumerate(productos_ordenados[:5], 1):
    barra = barra_horizontal(datos["ingresos"], maximo_producto, ancho=20)
    print(f"  {i}. {producto:<15} │{barra}│ {formatear_dinero(datos['ingresos'])}")
    print(f"      Unidades: {datos['unidades']:>4} | Transacciones: {datos['transacciones']:>4}")

# ============================================================
# PANEL 4: VENTAS POR PRODUCTO (COUNTER)
# ============================================================

titulo_seccion("FRECUENCIA DE COMPRA — TOP 5")

print()
max_transacciones = contador_transacciones.most_common(1)[0][1]
for producto, cantidad in contador_transacciones.most_common(5):
    barra = barra_horizontal(cantidad, max_transacciones, ancho=20, caracter="▪")
    print(f"  {producto:<15} │{barra}│ {cantidad:>3} ventas")

# ============================================================
# PANEL 5: DISTRIBUCIÓN MENSUAL (MINI HISTOGRAMA)
# ============================================================

titulo_seccion("TENDENCIA TRIMESTRAL")

trimestres = {
    "Q1 (Ene-Mar)": sum(ingresos_por_mes[m] for m in ["Ene", "Feb", "Mar"]),
    "Q2 (Abr-Jun)": sum(ingresos_por_mes[m] for m in ["Abr", "May", "Jun"]),
    "Q3 (Jul-Sep)": sum(ingresos_por_mes[m] for m in ["Jul", "Ago", "Sep"]),
    "Q4 (Oct-Dic)": sum(ingresos_por_mes[m] for m in ["Oct", "Nov", "Dic"]),
}

max_trimestre = max(trimestres.values())
print()
for trimestre, ingreso in trimestres.items():
    barra = barra_horizontal(ingreso, max_trimestre, ancho=25)
    porcentaje = (ingreso / ingreso_total) * 100
    print(f"  {trimestre} │{barra}│ {porcentaje:.1f}%")
    print(f"  {'':>13} {formatear_dinero(ingreso)}")

# ============================================================
# PANEL 6: ESTADÍSTICAS DESCRIPTIVAS
# ============================================================

titulo_seccion("ESTADÍSTICAS DESCRIPTIVAS")

importes = [v["precio"] * v["cantidad"] for v in ventas]
importes_sorted = sorted(importes)
n = len(importes)
mediana = importes_sorted[n//2] if n % 2 == 1 else (importes_sorted[n//2-1] + importes_sorted[n//2]) / 2

print(f"\n  Venta más alta:    {formatear_dinero(max(importes))}")
print(f"  Venta más baja:    {formatear_dinero(min(importes))}")
print(f"  Promedio:          {formatear_dinero(sum(importes)/n)}")
print(f"  Mediana:           {formatear_dinero(mediana)}")
print(f"  Ventas > $500:     {sum(1 for i in importes if i > 500):>10,}")
print(f"  Ventas <= $50:     {sum(1 for i in importes if i <= 50):>10,}")

print("\n" + "═"*60)
print("  Fin del Dashboard")
print("═"*60)

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Agrega un panel de "Comparativa año anterior"
# ────────────────────────────────────────────────────────────
# Genera datos para un año anterior (random.seed(99))
# Compara mes a mes con flechas: ↑ si mejoró, ↓ si bajó
# Muestra el % de cambio
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Dashboard interactivo
# ────────────────────────────────────
# Modifica el programa para que pregunte al usuario:
#   "¿Qué sección quieres ver? (1-6)"
# y muestre solo esa sección del dashboard.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Exportar a texto
# ──────────────────────────────
# Guarda todo el dashboard en un archivo "reporte_ventas.txt"
# usando sys.stdout y redirigiendo la salida.
# PISTA: import io, sys; buffer = io.StringIO()
#        sys.stdout = buffer → ejecutas el código → sys.stdout = sys.__stdout__
#        texto = buffer.getvalue() → guardas en archivo
#
# ESCRIBE TU CÓDIGO AQUÍ:
