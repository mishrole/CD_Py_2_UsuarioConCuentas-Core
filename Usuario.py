from CuentaBancaria import CuentaBancaria

class Usuario:
    def __init__(self, name = 'N/A', email = 'N/A'):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interés = 0.02, balance = 0)
    # Método Hacer Depósito
    def hacer_depósito(self, amount):
        self.cuenta.depósito(amount)
        return self
    # Método Hacer retiro
    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)
        return self
    # Método Mostrar Balance
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: {self.cuenta.balance:.2f}')
        return self