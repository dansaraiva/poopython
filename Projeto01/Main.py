class Main:
    pass

print("Teste do projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Daniel", "8599999-9999")
conta = Conta(c1.nome,1234,0)

print(conta.titular, " Numero:  " ,conta.numero, " Seu saldo: ", conta.saldo)

