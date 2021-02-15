# This program the rolling of dice
import random

MIN = 1
MAX = 6


def main():
    # Create variable to control the loop
    again = 'y'

    # simulate the rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # do another roll of dice
        again = input("Roll them again ?(Enter y for yes): ")


main()
