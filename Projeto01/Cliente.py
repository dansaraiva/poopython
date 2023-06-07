class Cliente:
    def __init__(self, n, fone):
        
        self._nome = n
        self._telefone = fone

    #GET
    def getNome(self):
        return self._nome
    
    #SET
    def setNome(self, nome):
        self._nome = nome
    
    