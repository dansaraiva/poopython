class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Daniel", "8599999-9999")
conta = Conta(c1._nome,1234,0)

conta.deposito(100)
conta.saque(50)
conta.extrato()

