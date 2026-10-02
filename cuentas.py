class CuentaBancaria:
    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = 0.0

    def depositar(self, monto):
        if monto > 0:
            self._saldo = self._saldo + monto
        else:
            raise ValueError("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo = self._saldo - monto

    def consultar_saldo(self):
        return self._saldo

    def __str__(self):
        return "Cuenta: " + str(self.numero_cuenta) + " | Titular: " + str(self.titular) + " | Saldo: S/ " + str(self._saldo)

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, tasa_interes):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        interes = (self.consultar_saldo() * self.tasa_interes) / 100
        return interes

    def __str__(self):
        base = super().__str__()
        return base + " | Tasa Interes: " + str(self.tasa_interes) + "% | Interes Anual: S/ " + str(self.calcular_interes())

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, limite_sobregiro):
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > (self.consultar_saldo() + self.limite_sobregiro):
            raise ValueError("El retiro excede el limite de sobregiro permitido.")
        self._saldo = self._saldo - monto

    def permite_sobregiro(self):
        if self.consultar_saldo() < 0:
            return True
        else:
            return False


# ejemplos de la IA
print("--- Cuenta Ahorros ---")
ahorros = CuentaAhorros("AH-001", "Juan Perez", 4.5)
ahorros.depositar(1000.0)
print(ahorros)

print("\n--- Cuenta Corriente ---")
corriente = CuentaCorriente("CC-002", "Maria Lopez", 500.0)
corriente.depositar(200.0)
print(corriente)

# Retiro con sobregiro
corriente.retirar(400.0)
print("Sobregiro activo: " + str(corriente.permite_sobregiro()))
print(corriente)