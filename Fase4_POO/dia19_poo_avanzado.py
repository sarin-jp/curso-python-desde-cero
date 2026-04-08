# ╔══════════════════════════════════════════════════════════╗
# ║  DÍA 19: POO AVANZADO — ENCAPSULAMIENTO Y PROPIEDADES ║
# ║  Fase 4: Programación Orientada a Objetos (POO)         ║
# ║  Duración: ~2 horas                                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📋 QUÉ VAS A APRENDER HOY:
#    - Encapsulamiento: proteger datos internos
#    - Atributos privados con __doble_guión
#    - @property: acceder a datos de forma controlada
#    - @staticmethod: métodos que no necesitan el objeto
#    - Clase CuentaBancaria completa con historial
#
# ▶️ CÓMO EJECUTAR ESTE ARCHIVO:
#    1. Abre este archivo en VS Code
#    2. Haz clic en el botón ▶️ (arriba a la derecha)
#    3. Mira la terminal de abajo
#
# 📝 QUÉ TIENES QUE HACER:
#    1. Lee todo el código y los comentarios
#    2. Ejecuta el programa
#    3. Experimenta con las propiedades
#    4. Haz los ejercicios del final
#
# ⏮️ ANTERIOR: dia18_proyecto_inventario.py
# ⏭️ SIGUIENTE: dia20_proyecto_banco.py
# ════════════════════════════════════════════════════════════

import datetime

# ============================================================
# SECCIÓN 1: ENCAPSULAMIENTO
# ============================================================

# El encapsulamiento "esconde" los datos internos de la clase.
# Evita que alguien modifique datos de forma incorrecta.
#
# En Python, usamos convenciones para indicar privacidad:
#   nombre_atributo   → público (accesible desde fuera)
#   _nombre_atributo  → "privado por convención" (desaconsejado, pero posible)
#   __nombre_atributo → privado real (Python cambia el nombre internamente)

class CuentaBancaria:
    """Cuenta bancaria con encapsulamiento completo."""

    # Atributo de clase (compartido por TODOS los objetos de esta clase):
    tasa_interes = 0.05  # 5% anual

    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        self.titular = titular
        self.__numero_cuenta = numero_cuenta  # Privado — no se puede acceder directamente
        self.__saldo = saldo_inicial           # Privado — solo se accede mediante métodos
        self.__historial = []                  # Privado — lista de movimientos

        if saldo_inicial > 0:
            self.__registrar_movimiento("Depósito inicial", saldo_inicial)

    # ============================================================
    # PROPIEDADES (@property): Acceso controlado a atributos privados
    # ============================================================

    @property
    def saldo(self):
        """Getter: permite LEER el saldo."""
        return self.__saldo

    @property
    def numero_cuenta(self):
        """Getter: muestra el número enmascarado."""
        return f"****{self.__numero_cuenta[-4:]}"

    @property
    def historial(self):
        """Getter: devuelve una copia del historial."""
        return self.__historial.copy()  # Copia para que no puedan modificar el original

    # ============================================================
    # MÉTODOS DE INSTANCIA
    # ============================================================

    def __registrar_movimiento(self, tipo, cantidad):
        """Método privado: registra un movimiento en el historial."""
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.__historial.append({
            "fecha": fecha,
            "tipo": tipo,
            "cantidad": cantidad,
            "saldo_resultante": self.__saldo
        })

    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva")
        self.__saldo += cantidad
        self.__registrar_movimiento("Depósito", cantidad)
        print(f"✅ Depósito de ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def retirar(self, cantidad):
        """Retira dinero de la cuenta."""
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        if cantidad > self.__saldo:
            raise ValueError(f"Saldo insuficiente. Saldo actual: ${self.__saldo:.2f}")
        self.__saldo -= cantidad
        self.__registrar_movimiento("Retiro", -cantidad)
        print(f"✅ Retiro de ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def aplicar_interes(self):
        """Aplica el interés anual al saldo."""
        interes = self.__saldo * self.tasa_interes
        self.__saldo += interes
        self.__registrar_movimiento("Interés anual", interes)
        print(f"✅ Interés aplicado: ${interes:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def mostrar_historial(self):
        """Muestra todos los movimientos de la cuenta."""
        print(f"\n{'='*55}")
        print(f"  Estado de cuenta: {self.titular}")
        print(f"  Cuenta: {self.numero_cuenta}")
        print(f"{'='*55}")
        print(f"  {'Fecha':<17} {'Tipo':<18} {'Cantidad':>10} {'Saldo':>10}")
        print(f"  {'-'*53}")

        for mov in self.__historial:
            cant = mov["cantidad"]
            signo = "+" if cant >= 0 else ""
            print(f"  {mov['fecha']:<17} {mov['tipo']:<18} "
                  f"{signo}${cant:>8.2f} ${mov['saldo_resultante']:>8.2f}")

        print(f"  {'-'*53}")
        print(f"  {'Saldo actual:':>40} ${self.__saldo:>8.2f}")
        print(f"{'='*55}")

    # ============================================================
    # MÉTODO ESTÁTICO (@staticmethod): No necesita self
    # ============================================================

    @staticmethod
    def validar_monto(monto):
        """Verifica si un monto es válido (no necesita acceder a ningún objeto)."""
        return isinstance(monto, (int, float)) and monto > 0

    @staticmethod
    def calcular_interes_compuesto(capital, tasa, años):
        """Calcula el interés compuesto."""
        return capital * (1 + tasa) ** años

    def __str__(self):
        return (f"Cuenta de {self.titular} | "
                f"Número: {self.numero_cuenta} | "
                f"Saldo: ${self.__saldo:.2f}")


# ============================================================
# USANDO LA CLASE
# ============================================================

print("=== Sistema de Cuentas Bancarias ===\n")

# Crear cuenta:
cuenta1 = CuentaBancaria("Ana García", "1234567890", 1000)
cuenta2 = CuentaBancaria("Carlos López", "0987654321", 500)

print(cuenta1)
print(cuenta2)

# Operaciones:
print("\n--- Operaciones en la cuenta de Ana ---")
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.depositar(1500)
cuenta1.retirar(100)
cuenta1.aplicar_interes()

# Ver historial:
cuenta1.mostrar_historial()

# Intentar acceso directo (fallará):
print("\n--- Intentando acceder directamente al saldo privado ---")
try:
    print(cuenta1.__saldo)
except AttributeError as e:
    print(f"❌ Error: {e}")
    print("   (El atributo __saldo es privado, no se puede acceder directamente)")

# Acceso correcto mediante @property:
print(f"\n✅ Saldo mediante @property: ${cuenta1.saldo:.2f}")

# Método estático (se puede llamar sin crear objeto):
print(f"\n--- Método estático ---")
print(f"¿'1500' es un monto válido? {CuentaBancaria.validar_monto(1500)}")
print(f"¿'-100' es un monto válido? {CuentaBancaria.validar_monto(-100)}")

capital = 10000
print(f"\n${capital} a 5% por 10 años = ${CuentaBancaria.calcular_interes_compuesto(capital, 0.05, 10):.2f}")

# ============================================================
# 🎯 EJERCICIOS — ¡Ahora te toca a ti!
# ============================================================
#
# EJERCICIO 1: Transferencias entre cuentas
# ──────────────────────────────────────────
# Agrega un método transferir(destino, cantidad) a CuentaBancaria.
# Este método retira de la cuenta actual y deposita en la cuenta destino.
# Registra en el historial de ambas cuentas.
# Si no hay saldo suficiente, lanza un ValueError.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 2: Fecha en el historial
# ────────────────────────────────────
# Modifica el historial para que también guarde la hora exacta
# en formato HH:MM:SS. Muéstrala en el estado de cuenta.
#
# ESCRIBE TU CÓDIGO AQUÍ:


# EJERCICIO 3: Clase Banco
# ─────────────────────────
# Crea una clase Banco que contenga varias CuentaBancaria.
# Atributos: nombre_banco, cuentas (lista)
# Métodos: crear_cuenta(), buscar_cuenta(numero), listar_cuentas(),
#          total_depósitos()
#
# ESCRIBE TU CÓDIGO AQUÍ:
