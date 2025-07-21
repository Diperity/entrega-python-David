class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular        # público
        self._tipo_cuenta = "ahorros" # protegido
        self.__saldo = saldo          # privado

    def ver_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Ana", 1000 )
print(cuenta.titular)        # Ana
print(cuenta.ver_saldo())    # 1000
# print(cuenta.__saldo)      # Error
