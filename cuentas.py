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