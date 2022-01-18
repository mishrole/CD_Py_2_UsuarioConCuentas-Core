from CuentaBancaria import CuentaBancaria

class Usuario:
    def __init__(self, nombre = 'N/A', email = 'N/A'):
        self.nombre = nombre
        self.email = email
        self.cuenta = [CuentaBancaria(tasa_interés = 0.02, balance = 0), CuentaBancaria(tasa_interés = 0.02, balance = 0)]
    # Método Hacer Depósito
    def hacer_depósito(self, indiceCuenta, monto):
        print('')
        if self.verificarCuenta(indiceCuenta):
            self.cuenta[indiceCuenta].depósito(monto)
        else:
            print(f'No se encontró la cuenta {indiceCuenta}')
        return self
    # Método Hacer retiro
    def hacer_retiro(self, indiceCuenta, monto):
        print('')
        if self.verificarCuenta(indiceCuenta):
            self.cuenta[indiceCuenta].retiro(monto)
        else:
            print(f'No se encontró la cuenta {indiceCuenta}')
        return self
    # Método Mostrar Balance
    def mostrar_balance_usuario(self):
        print('')
        print(f'Balance de Cuentas de {self.nombre}')
        print('- - - - - - - - - - - - - - - -')
        for cuenta in self.cuenta:
            print(f'Usuario: {self.nombre}, Balance: {cuenta.balance:.2f}')
        return self
    # Método Transferencia Externa
    def transferencia_externa(self, indiceCuentaOrigen, otro_usuario, indiceCuentaDestino, monto):
        print('')
        print('Transferencia Externa')
        print('- - - - - - - - - - - - - - - -')
        if self.verificarCuenta(indiceCuentaOrigen):
            if self.cuenta[indiceCuentaOrigen].balance - monto < 0:
                print('Fondos insuficientes')
            else:
                if otro_usuario.verificarCuenta(indiceCuentaDestino):
                    print(f'Realizando una transferencia de {monto:.2f}')
                    print(f'Origen: Cuenta {indiceCuentaOrigen} de {self.nombre}')
                    print(f'Destino: Cuenta {indiceCuentaDestino} de {otro_usuario.nombre}')
                    self.cuenta[indiceCuentaOrigen].balance -= monto
                    otro_usuario.cuenta[indiceCuentaDestino].balance += monto
                else:
                    print(f'No se encontró la cuenta {indiceCuentaDestino} de {otro_usuario.nombre}') 
        else:
            print(f'No se encontró la cuenta {indiceCuentaOrigen} de {self.nombre}') 
        return self
    def verificarCuenta(self, indiceCuenta):
        if len(self.cuenta) - 1 >= indiceCuenta:
            return True
        
        return False