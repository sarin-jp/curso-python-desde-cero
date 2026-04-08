# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 18: PROYECTO — SISTEMA DE INVENTARIO             ║
# ║  Fase 4: Programación Orientada a Objetos (POO)         ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Aplicar POO en un proyecto real
#    - Clase Producto: representa un artículo en el inventario
#    - Clase Inventario: gestiona una colección de productos
#    - Buscar, agregar, actualizar y eliminar productos
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Sigue el menú del inventario
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código
#    2. Ejecuta el programa
#    3. Agrega tus propios productos
#    4. Haz los ejercicios de extensión
#
# ⏮️ ANTERIOR: dia17_herencia.py
# ⏭️ SIGUIENTE: dia19_poo_avanzado.py
# ════════════════════════════════════════════════════════════

# ============================================================
# CLASE PRODUCTO
# ============================================================

class Producto:
    """Representa un producto en el inventario."""

    def __init__(self, codigo, nombre, precio, cantidad, categoria="General"):
        self.codigo = codigo.upper()
        self.nombre = nombre.title()
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def valor_total(self):
        """Calcula el valor total del stock de este producto."""
        return self.precio * self.cantidad

    def agregar_stock(self, cantidad):
        """Agrega unidades al inventario."""
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"✅ +{cantidad} unidades de '{self.nombre}'. Total: {self.cantidad}")
        else:
            print("❌ La cantidad debe ser positiva")

    def retirar_stock(self, cantidad):
        """Retira unidades del inventario."""
        if cantidad <= 0:
            print("❌ La cantidad debe ser positiva")
        elif cantidad > self.cantidad:
            print(f"❌ Stock insuficiente. Hay {self.cantidad} unidades de '{self.nombre}'")
        else:
            self.cantidad -= cantidad
            print(f"✅ -{cantidad} unidades de '{self.nombre}'. Restante: {self.cantidad}")

    def esta_en_stock(self):
        """Devuelve True si hay al menos 1 unidad."""
        return self.cantidad > 0

    def __str__(self):
        """Representación como texto del producto."""
        estado = "✅" if self.esta_en_stock() else "❌ AGOTADO"
        return (f"[{self.codigo}] {self.nombre:<25} "
                f"${self.precio:>8.2f}  "
                f"Stock: {self.cantidad:>5}  "
                f"Valor: ${self.valor_total():>10.2f}  {estado}")


# ============================================================
# CLASE INVENTARIO
# ============================================================

class Inventario:
    """Gestiona una colección de productos."""

    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = {}  # Diccionario: codigo → Producto

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        if producto.codigo in self.productos:
            print(f"❌ Ya existe un producto con código {producto.codigo}")
        else:
            self.productos[producto.codigo] = producto
            print(f"✅ Producto '{producto.nombre}' agregado al inventario")

    def buscar_por_codigo(self, codigo):
        """Busca un producto por su código."""
        return self.productos.get(codigo.upper(), None)

    def buscar_por_nombre(self, nombre):
        """Busca productos que contengan el nombre dado."""
        nombre_lower = nombre.lower()
        resultados = [p for p in self.productos.values()
                      if nombre_lower in p.nombre.lower()]
        return resultados

    def eliminar_producto(self, codigo):
        """Elimina un producto del inventario."""
        codigo = codigo.upper()
        if codigo in self.productos:
            nombre = self.productos[codigo].nombre
            del self.productos[codigo]
            print(f"✅ Producto '{nombre}' eliminado")
        else:
            print(f"❌ No existe producto con código {codigo}")

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("📭 El inventario está vacío")
            return

        print(f"\n{'='*70}")
        print(f"  📦 INVENTARIO — {self.nombre_tienda}")
        print(f"{'='*70}")
        print(f"{'Código':<8} {'Nombre':<25} {'Precio':>10} {'Stock':>7} {'Valor Total':>12}")
        print(f"{'-'*70}")

        for producto in self.productos.values():
            print(producto)

        print(f"{'-'*70}")
        print(f"  Total de productos: {self.total_productos()}")
        print(f"  Valor total del inventario: ${self.valor_total_inventario():,.2f}")
        print(f"{'='*70}")

    def productos_agotados(self):
        """Devuelve lista de productos sin stock."""
        return [p for p in self.productos.values() if not p.esta_en_stock()]

    def total_productos(self):
        """Devuelve el número de tipos de productos."""
        return len(self.productos)

    def valor_total_inventario(self):
        """Calcula el valor total de todo el inventario."""
        return sum(p.valor_total() for p in self.productos.values())

    def productos_por_categoria(self, categoria):
        """Devuelve productos de una categoría específica."""
        return [p for p in self.productos.values()
                if p.categoria.lower() == categoria.lower()]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def menu_inventario(inv):
    """Muestra el menú de opciones."""
    print(f"\n{'─'*40}")
    print(f"  🏪 {inv.nombre_tienda}")
    print(f"  Productos: {inv.total_productos()}")
    print(f"  Valor total: ${inv.valor_total_inventario():,.2f}")
    print(f"{'─'*40}")
    print("  1. Ver todos los productos")
    print("  2. Agregar producto nuevo")
    print("  3. Buscar producto")
    print("  4. Agregar stock")
    print("  5. Retirar stock")
    print("  6. Ver productos agotados")
    print("  7. Eliminar producto")
    print("  0. Salir")


# Crear inventario y cargar productos de ejemplo:
inventario = Inventario("Mi Tienda de Tecnología")

# Productos de ejemplo:
productos_iniciales = [
    Producto("LAP001", "Laptop HP 15", 799.99, 10, "Computadoras"),
    Producto("MON001", "Monitor Samsung 24\"", 299.99, 15, "Periféricos"),
    Producto("TEC001", "Teclado Mecánico RGB", 89.99, 25, "Periféricos"),
    Producto("RAT001", "Mouse Inalámbrico", 39.99, 30, "Periféricos"),
    Producto("AUD001", "Audífonos Bluetooth", 149.99, 8, "Audio"),
    Producto("USB001", "USB-C Hub 7 puertos", 49.99, 0, "Accesorios"),  # Agotado
]

for p in productos_iniciales:
    inventario.agregar_producto(p)

print("\n🎉 Inventario cargado con productos de ejemplo.")

# Menú principal:
while True:
    menu_inventario(inventario)
    opcion = input("\nElige una opción: ").strip()

    if opcion == "1":
        inventario.mostrar_todos()

    elif opcion == "2":
        print("\n── Agregar nuevo producto ──")
        codigo = input("Código (ej: PROD001): ").strip()
        nombre = input("Nombre: ").strip()

        try:
            precio = float(input("Precio: $"))
            cantidad = int(input("Cantidad inicial: "))
        except ValueError:
            print("❌ Precio y cantidad deben ser números")
            continue

        categoria = input("Categoría (Enter para 'General'): ").strip() or "General"
        nuevo = Producto(codigo, nombre, precio, cantidad, categoria)
        inventario.agregar_producto(nuevo)

    elif opcion == "3":
        termino = input("Buscar (código o nombre): ").strip()

        # Intentar por código primero
        resultado = inventario.buscar_por_codigo(termino)
        if resultado:
            print(f"\nProducto encontrado:\n{resultado}")
        else:
            # Buscar por nombre
            resultados = inventario.buscar_por_nombre(termino)
            if resultados:
                print(f"\n{len(resultados)} productos encontrados:")
                for p in resultados:
                    print(f"  {p}")
            else:
                print("❌ No se encontraron productos")

    elif opcion == "4":
        codigo = input("Código del producto: ").strip()
        producto = inventario.buscar_por_codigo(codigo)
        if producto:
            try:
                cantidad = int(input(f"Cantidad a agregar a '{producto.nombre}': "))
                producto.agregar_stock(cantidad)
            except ValueError:
                print("❌ Escribe un número válido")
        else:
            print(f"❌ Producto {codigo} no encontrado")

    elif opcion == "5":
        codigo = input("Código del producto: ").strip()
        producto = inventario.buscar_por_codigo(codigo)
        if producto:
            try:
                cantidad = int(input(f"Cantidad a retirar de '{producto.nombre}': "))
                producto.retirar_stock(cantidad)
            except ValueError:
                print("❌ Escribe un número válido")
        else:
            print(f"❌ Producto {codigo} no encontrado")

    elif opcion == "6":
        agotados = inventario.productos_agotados()
        if agotados:
            print(f"\n❌ Productos agotados ({len(agotados)}):")
            for p in agotados:
                print(f"  [{p.codigo}] {p.nombre}")
        else:
            print("✅ No hay productos agotados")

    elif opcion == "7":
        codigo = input("Código del producto a eliminar: ").strip()
        inventario.eliminar_producto(codigo)

    elif opcion == "0":
        print("\n👋 Cerrando el sistema de inventario.")
        break

    else:
        print("❌ Opción no válida")
