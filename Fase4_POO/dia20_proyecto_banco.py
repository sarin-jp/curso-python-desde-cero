# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 20: PROYECTO — SISTEMA BANCARIO COMPLETO         ║
# ║  Fase 4: Programación Orientada a Objetos (POO)         ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Aplicar todo lo aprendido en POO
#    - Sistema bancario con clase Cuenta y clase Banco
#    - Menú completo con todas las operaciones
#    - Validaciones y manejo de errores
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Sigue el menú del banco
#
# ⏮️ ANTERIOR: dia19_poo_avanzado.py
# ⏭️ SIGUIENTE: ../Fase5_Archivos_y_Librerias/dia21_archivos_texto.py
# ════════════════════════════════════════════════════════════

import datetime
import random

# ============================================================
# CLASE CUENTA
# ============================================================

class Cuenta:
    """Representa una cuenta bancaria."""

    def __init__(self, numero, titular, tipo="Ahorros", saldo_inicial=0.0):
        self.numero = numero
        self.titular = titular
        self.tipo = tipo
        self.__saldo = float(saldo_inicial)
        self.__movimientos = []
        self.activa = True

        if saldo_inicial > 0:
            self._agregar_movimiento("Apertura", saldo_inicial)

    @property
    def saldo(self):
        return self.__saldo

    def _agregar_movimiento(self, tipo, monto):
        self.__movimientos.append({
            "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "tipo": tipo,
            "monto": monto,
            "saldo": self.__saldo
        })

    def depositar(self, monto):
        if not self.activa:
            raise Exception("La cuenta está inactiva")
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto
        self._agregar_movimiento("Depósito", monto)
        return monto

    def retirar(self, monto):
        if not self.activa:
            raise Exception("La cuenta está inactiva")
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.__saldo:
            raise ValueError(f"Saldo insuficiente (${self.__saldo:.2f})")
        self.__saldo -= monto
        self._agregar_movimiento("Retiro", -monto)
        return monto

    def transferir_a(self, cuenta_destino, monto):
        self.retirar(monto)
        cuenta_destino.depositar(monto)
        self._agregar_movimiento(f"Transferencia a {cuenta_destino.numero}", -monto)
        cuenta_destino._agregar_movimiento(f"Transferencia de {self.numero}", monto)

    def ver_movimientos(self):
        return self.__movimientos.copy()

    def __str__(self):
        estado = "Activa" if self.activa else "Inactiva"
        return (f"Cuenta #{self.numero} ({self.tipo}) | "
                f"Titular: {self.titular} | "
                f"Saldo: ${self.__saldo:.2f} | {estado}")


# ============================================================
# CLASE BANCO
# ============================================================

class Banco:
    """Gestiona múltiples cuentas bancarias."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.__cuentas = {}  # numero → Cuenta

    def _generar_numero(self):
        """Genera un número de cuenta único."""
        while True:
            numero = str(random.randint(10000000, 99999999))
            if numero not in self.__cuentas:
                return numero

    def crear_cuenta(self, titular, tipo="Ahorros", saldo_inicial=0.0):
        """Crea y registra una nueva cuenta."""
        numero = self._generar_numero()
        cuenta = Cuenta(numero, titular, tipo, saldo_inicial)
        self.__cuentas[numero] = cuenta
        print(f"✅ Cuenta creada. Número: {numero}")
        return cuenta

    def buscar_cuenta(self, numero):
        """Busca una cuenta por número."""
        return self.__cuentas.get(numero, None)

    def listar_cuentas(self):
        """Muestra todas las cuentas."""
        if not self.__cuentas:
            print("📭 No hay cuentas registradas")
            return
        print(f"\n{'═'*65}")
        print(f"  🏦 {self.nombre} — {len(self.__cuentas)} cuentas")
        print(f"{'═'*65}")
        for cuenta in self.__cuentas.values():
            print(f"  {cuenta}")
        total = sum(c.saldo for c in self.__cuentas.values())
        print(f"{'─'*65}")
        print(f"  {'Total en el banco:':>50} ${total:>10.2f}")
        print(f"{'═'*65}")

    def total_en_banco(self):
        return sum(c.saldo for c in self.__cuentas.values())


# ============================================================
# FUNCIONES DE MENÚ
# ============================================================

def solicitar_cuenta(banco, mensaje="Número de cuenta: "):
    """Pide un número de cuenta y lo valida."""
    numero = input(mensaje).strip()
    cuenta = banco.buscar_cuenta(numero)
    if not cuenta:
        print(f"❌ No existe la cuenta {numero}")
    return cuenta


def solicitar_monto(mensaje="Monto: $"):
    """Pide un monto y lo valida."""
    try:
        monto = float(input(mensaje))
        if monto <= 0:
            print("❌ El monto debe ser positivo")
            return None
        return monto
    except ValueError:
        print("❌ Ingresa un número válido")
        return None


def menu_principal(banco):
    print(f"\n{'─'*45}")
    print(f"  🏦 {banco.nombre}")
    print(f"  Total en banco: ${banco.total_en_banco():,.2f}")
    print(f"{'─'*45}")
    print("  1. Crear cuenta nueva")
    print("  2. Ver mis datos y saldo")
    print("  3. Depositar dinero")
    print("  4. Retirar dinero")
    print("  5. Transferir a otra cuenta")
    print("  6. Ver movimientos")
    print("  7. Listar todas las cuentas")
    print("  0. Salir")


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

banco = Banco("Banco Python Nacional")

# Cuentas de ejemplo:
c1 = banco.crear_cuenta("María García", "Ahorros", 5000)
c2 = banco.crear_cuenta("Carlos López", "Corriente", 2500)
c3 = banco.crear_cuenta("Ana Martínez", "Ahorros", 10000)

print(f"\n🎉 Bienvenido al sistema bancario de {banco.nombre}")

while True:
    menu_principal(banco)
    opcion = input("\nElige una opción: ").strip()

    if opcion == "1":
        print("\n── Crear cuenta nueva ──")
        titular = input("Nombre del titular: ").strip()
        tipo = input("Tipo (Ahorros/Corriente) [Enter=Ahorros]: ").strip() or "Ahorros"
        saldo = solicitar_monto("Saldo inicial: $") or 0
        banco.crear_cuenta(titular, tipo, saldo)

    elif opcion == "2":
        cuenta = solicitar_cuenta(banco)
        if cuenta:
            print(f"\n{cuenta}")

    elif opcion == "3":
        cuenta = solicitar_cuenta(banco)
        if cuenta:
            monto = solicitar_monto()
            if monto:
                try:
                    cuenta.depositar(monto)
                    print(f"  Nuevo saldo: ${cuenta.saldo:.2f}")
                except Exception as e:
                    print(f"❌ {e}")

    elif opcion == "4":
        cuenta = solicitar_cuenta(banco)
        if cuenta:
            monto = solicitar_monto()
            if monto:
                try:
                    cuenta.retirar(monto)
                    print(f"  Nuevo saldo: ${cuenta.saldo:.2f}")
                except Exception as e:
                    print(f"❌ {e}")

    elif opcion == "5":
        origen = solicitar_cuenta(banco, "Cuenta origen: ")
        destino = solicitar_cuenta(banco, "Cuenta destino: ")
        if origen and destino:
            monto = solicitar_monto()
            if monto:
                try:
                    origen.transferir_a(destino, monto)
                    print(f"✅ Transferencia de ${monto:.2f} exitosa")
                except Exception as e:
                    print(f"❌ {e}")

    elif opcion == "6":
        cuenta = solicitar_cuenta(banco)
        if cuenta:
            movs = cuenta.ver_movimientos()
            if movs:
                print(f"\n{'─'*60}")
                print(f"  Movimientos de la cuenta {cuenta.numero}")
                print(f"{'─'*60}")
                for m in movs:
                    signo = "+" if m["monto"] >= 0 else ""
                    print(f"  {m['fecha']}  {m['tipo']:<30} {signo}${m['monto']:>8.2f}")
                print(f"{'─'*60}")
            else:
                print("  No hay movimientos")

    elif opcion == "7":
        banco.listar_cuentas()

    elif opcion == "0":
        print("\n" + "╔" + "═"*48 + "╗")
        print("║" + "  🎉 ¡FELICITACIONES!  ".center(48) + "║")
        print("║" + "  Completaste la FASE 4: POO  ".center(48) + "║")
        print("║" + "  ".center(48) + "║")
        print("║" + "  Lo que aprendiste:  ".center(48) + "║")
        print("║" + "  ✅ Clases y objetos  ".center(48) + "║")
        print("║" + "  ✅ Herencia y polimorfismo  ".center(48) + "║")
        print("║" + "  ✅ Encapsulamiento  ".center(48) + "║")
        print("║" + "  ✅ @property y @staticmethod  ".center(48) + "║")
        print("║" + "  ".center(48) + "║")
        print("║" + "  La Fase 5 te espera:  ".center(48) + "║")
        print("║" + "  🔴 Archivos, JSON, APIs  ".center(48) + "║")
        print("╚" + "═"*48 + "╝")
        break

    else:
        print("❌ Opción no válida")
