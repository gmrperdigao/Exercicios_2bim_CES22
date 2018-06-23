### Nesse exemplo criamos uma classe roupa com o método sew(String tecido) para fazer a roupa com determinado tecido
### Nós podemos criar múltiplas folhas como Calça, Jaqueta, Camisa, etc.


import abc

class Roupa(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sew(self, tecido):
        pass

class Jaqueta(Roupa):
    def sew(self, tecido):
        print("Costurando uma jaqueta de " + tecido)

class Calca(Roupa):
    def sew(self, tecido):
        print("Costurando uma calca de " + tecido)

class Sewing(Roupa):
    def __init__(self):
        self.roupas = []

    def sew(self, tecido):
        for r in self.roupas:
            r.sew(tecido)

    def add(self, r):
        self.roupas.append(r)

    def remove(self, r):
        self.roupas.remove(r)

    def clear(self):
        print("Retirando todas as peças costuradas")
        self.roupas = []

if __name__ == '__main__':
    jaq1 = Jaqueta()
    jaq2 = Jaqueta()
    cal = Calca()

    sewing = Sewing()
    sewing.add(jaq1)
    sewing.add(jaq2)
    sewing.add(cal)

    sewing.sew("Jeans")

    sewing.clear()

    sewing.add(jaq1)
    sewing.add(cal)
    sewing.sew("Moletom")