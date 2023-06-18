from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        Veiculo.__init__(self, tipo, modelo, km)
        self.portas = portas

    def exibe(self):
        print("Tipo: ", self.tipo, "\nModelo: ", self.modelo, "com", self.km, "km rodados e", self.portas, "portas.")
        
        