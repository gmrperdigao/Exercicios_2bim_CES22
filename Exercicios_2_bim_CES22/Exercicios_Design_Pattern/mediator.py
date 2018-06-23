import random
import time


class ControlStock(object):

    def __init__(self):
        self.available_shelves = list()
        self.engaged_shelves = list()

    def authorize_replacement(self):
        if not self.available_shelves:
            print("Request denied. No available shelves")
            return False

        else:
            shelf = self.available_shelves.pop()
            self.engaged_shelves.append(shelf)
            print("Request granted. Please replace on the shelf {}".format(shelf))
            self.status()
            return True

    def authorize_drain(self):
        time.sleep(random.randint(0, 2))
        shelf = self.engaged_shelves.pop()
        self.available_shelves.append(shelf)
        self.status()

    def status(self):
        print(
            "The stock has {} available shelves/s".format(
                len(self.available_shelves)
            )
        )


class Product(object):

    def __init__(self):
        self.control_stock = None

    @property
    def registered(self):
        return True if self.control_stock is not None else False

    def register(self, control_stock):
        self.control_stock = control_stock
        print("A problem with the stock")

    def request_replacement(self):
        is_authorized = self.control_stock.authorize_replacement()
        if is_authorized:
            self.replace()

    def replace(self):
        print("The product {} is replaced".format(self))

    def drain(self):
        print("The product {} is drained out".format(self))
        self.control_stock.authorize_drain()


class Shelf(object):

    def register(self, control_stock):
        print("A shelf has been registered with the control stock")
        control_stock.available_shelves.append(self)
        control_stock.status()


def main():
    print("There is a market with 2 shelves and a controler\n")
    r1 = Shelf()
    r2 = Shelf()
    ct = ControlStock()
    r1.register(ct)
    r2.register(ct)

    print("\nWe need to receive 3 new products")
    a1 = Product()
    a2 = Product()
    a3 = Product()
    a1.register(ct)
    a2.register(ct)
    a3.register(ct)

    print(
        "\n2 new products are needed. There are enough shelves, so "
        "the requests are granted"
    )
    a1.request_replacement()
    a2.request_replacement()

    print(
        "\nThere are no shelves avaiable for the third product, so the request is denied"
    )
    a3.request_replacement()

    print(
        "\nThe first product is sold, so now the third "
        "product can be stocked"
    )
    a1.drain()
    a3.request_replacement()


if __name__ == "__main__":
    main()