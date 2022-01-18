from Usuario import Usuario

user = Usuario("Mitchell")
user.hacer_depósito(500).mostrar_balance_usuario()
user.hacer_retiro(100).mostrar_balance_usuario()

userB = Usuario("Gabriel")
userB.hacer_depósito(100).mostrar_balance_usuario()

user.transferencia_externa(userB, 100).mostrar_balance_usuario()
userB.mostrar_balance_usuario()