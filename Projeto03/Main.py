from Sub import Sub
from Subsub import Subsub
from Super import Super


class Main:
    pass

teste = Super()
teste.hello()

teste = Sub()
teste.hello()

teste = Subsub()
teste.hello()