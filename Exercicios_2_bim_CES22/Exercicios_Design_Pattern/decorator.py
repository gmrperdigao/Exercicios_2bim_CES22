import abc

class Trip(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def organizing(self):
        pass


class BasicTrip(Trip):
    def organizing(self):
        print("Basic Trip.")


class TripDecorator(Trip):
    def __init__(self, trip):
        self.trip = trip

    def organizing(self):
        self.trip.organizing()


class FunnyTrip(TripDecorator):
    def __init__(self, trip):
        super(FunnyTrip, self).__init__(trip)

    def organizing(self):
        super(FunnyTrip, self).organizing()
        print("Chosing locations to have a funny trip.")


class LuxuryTrip(TripDecorator):
    def __init__(self, trip):
        super(LuxuryTrip, self).__init__(trip)

    def organizing(self):
        super(LuxuryTrip, self).organizing()
        print("Chosing locations to have a luxury trip.")


if __name__ == '__main__':
    funny_trip = FunnyTrip(BasicTrip())
    funny_trip.organizing()
    print("-----")

    funny_luxury_trip = FunnyTrip(LuxuryTrip(BasicTrip()))
    funny_luxury_trip.organizing()