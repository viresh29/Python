import random

# The coin class simulates a coin that can be flipped


class Coin:

    # The __init__ method initializes the sideup data attributes with "Heads".

    def __init__(self):
        self.__sideup = 'Heads'

        # The toss method generates a random number in the range 0 through 1.
        # If the number is 0, then sideup set to 'Heads' else 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

        # The get_sideup method returns the value ref by sideup

    def get_sideup(self):
        return self.__sideup
