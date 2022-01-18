from Usuario import Usuario

mitchell = Usuario("Mitchell")
mitchell.hacer_depósito(0, 1000).hacer_depósito(1, 200).mostrar_balance_usuario()
mitchell.hacer_retiro(0, 20).hacer_retiro(1, 50).mostrar_balance_usuario()

gabriel = Usuario("Gabriel")
gabriel.hacer_depósito(0, 50).mostrar_balance_usuario()

# Transferencia entre cuentas de dos usuarios diferentes
mitchell.transferencia_externa(0, gabriel, 1, 500).mostrar_balance_usuario()
gabriel.mostrar_balance_usuario()

# Transferencia entre cuentas del mismo usuario
gabriel.transferencia_externa(0, gabriel, 1, 20).mostrar_balance_usuario()