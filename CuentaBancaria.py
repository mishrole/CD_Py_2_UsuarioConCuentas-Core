class CuentaBancaria:
    todas_las_cuentas = []
    def __init__(self, tasa_interés, balance = 0):
        self.tasa_interés = tasa_interés
        self.balance = balance
        self.tarifa = 5
        CuentaBancaria.todas_las_cuentas.append(self)
    def depósito(self, amount):
        print(f'Haciendo un depósito de {amount:.2f}')
        self.balance += amount
        return self
    def retiro(self, amount):
        if(self.balance - amount < 0):
            print("Fondos insuficientes")
        else:
            print(f'Realizando un retiro de {amount:.2f}')
            print(f'Cobrando una tarifa de {self.tarifa:.2f}')
            self.balance -= amount + self.tarifa
        return self
    def mostrar_info_cuenta(self):
        print(f'Balance: {self.balance:.2f}')
        return self
    def generar_interés(self):
        if(self.balance > 0):
            interes = self.balance * self.tasa_interés
            self.balance += interes
            print(f'Generando un interés de {interes:.2f}')
        else:
            print('Balance negativo, no genera interés')
        return self
    @classmethod
    def toda_la_info(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f'Instancia: {cuenta} | Tasa de Interés: {cuenta.tasa_interés:.2f} | Balance: {cuenta.balance:.2f}')