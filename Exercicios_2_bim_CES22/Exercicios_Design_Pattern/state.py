# States of a cellphone

class CellphoneState(object):
    """ Abstract base class of state of a cellphone """
    
    name = "state"
    allowed = []
    
    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print ('Current:',self,' => switched to new state',state.name)         
            self.__class__ = state
        else:
            print ('Current:',self,' => switching to',state.name,'not possible.')

    def __str__(self):
        return self.name
    
class Off(CellphoneState):
    """ State being switched off """

    name = "off"
    allowed = ['on']

class On(CellphoneState):
    """ State of being powered on and working """

    name = "on"
    allowed = ['off','calling','texting']

class Calling(CellphoneState):
    """ State of being in a calling after switched on """

    name = "calling"
    allowed = ['on']

class Texting(CellphoneState):
    """ State of using the cellphone to text messages """

    name = "texting"
    allowed = ['on']

class Cellphone(object):
    """ A class representing a cellphone """

    def __init__(self, model='HP'):
        self.model = model
        # State of the cellphone - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """

        self.state.switch(state)

if __name__ == "__main__":
    cell = Cellphone()
    # Switch on
    cell.change(On)
    # Switch off
    cell.change(Off)

    # Switch on again
    cell.change(On)
    # Start a calling
    cell.change(Calling)
    # Try to text - cannot!
    cell.change(Texting)
    # switch on back
    cell.change(On)
    # Finally off
    cell.change(Off)