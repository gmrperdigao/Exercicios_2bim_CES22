### O Padrão Ponte vai ser demonstrado num exemplo em que uma camisa pode ser tingida
### de diferentes cores usando a mesma classe abstrata, mas com diferentes classes implementadas por ponte

"O exemplo inclui os seguintes elementos"
### Modelo (abstração)
### Camisa (abstração refinada)
### Regata (abstração refinada)
### Cor (implementador)
### Amarelo (ImplementadorConcreto)
### Verde (ImplementadorConcreto)

import abc

class Cor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill_cor(self):
        pass

class Modelo(metaclass=abc.ABCMeta):
    def __init__(self, cor):
        self.cor = cor

    @abc.abstractmethod
    def cor_it(self):
        pass

class Camisa(Modelo):
    def __init__(self, cor):
        super(Camisa, self).__init__(cor)

    def cor_it(self):
        print("Camisa tingida de ", end="")
        self.cor.fill_cor()

class Regata(Modelo):
    def __init__(self, cor):
        super(Regata, self).__init__(cor)

    def cor_it(self):
        print("Regata tingida de ", end="")
        self.cor.fill_cor()

class Amarelo(Cor):
    def fill_cor(self):
        print("amarelo")

class Verde(Cor):
    def fill_cor(self):
        print("verde")

if __name__ == '__main__':
    s1 = Camisa(Amarelo())
    s1.cor_it()

    s2 = Regata(Verde())
    s2.cor_it()