import abc

class Evento(abc.ABC):

    @abc.abstractmethod
    def cadastrar(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

class Cientifico(Evento):
    def __init__(self):
        self.eventos = []



class Selecao(Evento):
    def __init__(self):
       self.selecao = []
#     pass
