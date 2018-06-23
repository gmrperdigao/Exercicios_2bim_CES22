import abc

# create an interface for Shapes
class Size(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bake(self):
        pass

# create an interface for flavours
class Flavour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill(self):
        pass


# create an abstract class to get factories for flavours and sizes objects
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_flavour(self):
        pass

    @abc.abstractmethod
    def get_size(self):
        pass


class Small(Size):
    def bake(self):
        print("Small::bake() method.")

class Medium(Size):
    def bake(self):
        print("Medium::bake() method.")

class Large(Size):
    def bake(self):
        print("Large::bake() method.")


class Pepperonni(Flavour):
    def fill(self):
        print("Pepperonni::fill() method.")

class Cheese(Flavour):
    def fill(self):
        print("Cheese::fill() method.")

class Margherita(Flavour):
    def fill(self):
        print("Margherita::fill() method.")


# create Factory classes extending AbstractFactory 
# to generate object of concrete class based on given information.
class SizeFactory(AbstractFactory):
    def get_size(self, size_type):
        if size_type == None:
            return None

        if size_type == "LARGE":
            return Large()
        elif size_type == "SMALL":
            return Small()
        elif size_type == "MEDIUM":
            return Small()

        return None

    def get_flavour(self):
        return None


class FlavourFactory(AbstractFactory):
    def get_flavour(self, flavour_type):
        if flavour_type == None:
            return None

        if flavour_type == "PEPPERONNI":
            return Pepperonni()
        elif flavour_type == "CHEESE":
            return Cheese()
        elif flavour_type == "MARGHERITA":
            return Margherita()

        return None

    def get_size(self):
        return None


# create a Factory generator/producer class 
# to get factories by passing an information such as size and flavour
class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice == "SIZE":
            return SizeFactory()
        elif choice == "FLAVOUR":
            return FlavourFactory()
        return None


if __name__ == '__main__':
    size_factory = FactoryProducer.get_factory("SIZE")

    size1 = size_factory.get_size("LARGE")
    size1.bake()

    size2 = size_factory.get_size("SMALL")
    size2.bake()

    size3 = size_factory.get_size("MEDIUM")
    size3.bake()

    flavour_factory = FactoryProducer.get_factory("FLAVOUR")

    flavour1 = flavour_factory.get_flavour("PEPPERONNI")
    flavour1.fill()

    flavour2 = flavour_factory.get_flavour("CHEESE")
    flavour2.fill()

    flavour3 = flavour_factory.get_flavour("MARGHERITA")
    flavour3.fill()