'''
    roll_dice
    ~~~~~~~~~

    Roll dice (and optionally weigh them, specifying the weight.)
'''



import random
import argparse



class Dice(object):

    def __init__(self, sides, side_weighted=None, weight=None, num_dice=1, sort=False):

        self.num_dice = num_dice
        self.sides = sides
        self.side_weighted = side_weighted
        self.weight = weight
        self.sort = sort

        if self.side_weighted is None and self.weight is not None:
            raise ValueError('Must specify a side to weigh if providing a self.weight.')

        if self.side_weighted > self.sides:
            raise ValueError('The weighted side must be between 1 and the number of sides on the die.')

        if self.sides < 1 or self.side_weighted < 1 and self.side_weighted is not None:
            raise ValueError('Die values must be greater than 0.')

        if self.weight is None:
            self.weight = self.sides

        if self.weight == 1:
            self.numbers = [self.side_weighted]

        elif self.weight < 1:
            self.numbers = [n for n in range(1, self.sides+1) if n is not self.side_weighted]

        elif self.side_weighted == None or self.weight == self.sides:
            self.numbers = [n for n in range(1, self.sides+1)]

        else:
            self.numbers = sum([[n] * (self.weight-1) + [self.side_weighted] for n in range(1, self.sides+1) if n is not side_weighted], [])


    def roll(self):
        '''
        Prints the rolls for the dice.
        '''

        rolls = []
        for _ in range(self.num_dice):
            r = random.choice(self.numbers)
            rolls.append(r)

        if self.sort == True:
            rolls = sorted(rolls, reverse=True)

        for i, r in enumerate(rolls):
            print("Die {}: {}".format(i+1, r))


def roll_die(num_sides, side_weighted=None, weight=None, debug=False):
    '''
    Given number of sides to the die, the (optional) side that is weighted,
    and the weight of that side, returns the roll.
    '''

    if side_weighted is None and weight is not None:
        raise ValueError('Must specify a side to weigh if providing a weight.')

    if side_weighted > num_sides:
        raise ValueError('The weighted side must be between 1 and the number of sides on the die.')

    if num_sides < 1 or side_weighted < 1 and side_weighted is not None:
        raise ValueError('Die values must be greater than 0.')

    '''-----------------------------------------------------------------------'''

    if weight is None:
        weight = num_sides

    if weight == 1:
        numbers = [side_weighted]

    elif weight < 1:
        numbers = [n for n in range(1, num_sides+1) if n is not side_weighted]

    elif side_weighted == None or weight == num_sides:
        numbers = [n for n in range(1, num_sides+1)]

    else:
        numbers = sum([[n] * (weight-1) + [side_weighted] for n in range(1, num_sides+1) if n is not side_weighted], [])


    roll = random.choice(numbers)

    return (roll, numbers)


def gen_parser():
    '''
    Creates command-line parser to access dice values.
    '''

    parser = argparse.ArgumentParser(description='Roll dice (and optionally weigh them, specifying the weight.)')
    parser.add_argument('number_sides', type=int, help='Number of sides each die has.')
    parser.add_argument('-d', '--dice', dest='number_dice', required=False, nargs='?', default=1, type=int, help='Number of dice to roll.')
    parser.add_argument('-w', '--weigh', dest='side_weighted', required=False, nargs='?', default=None, type=int, help='Weigh the die for this side.')
    parser.add_argument('-p', '-1/', '--prob', dest='weight', required=False, nargs='?', default=None, type=int, help='The probability the weighed side will be rolled.\n1/x rolls will be the weighted roll.')
    parser.add_argument('-s', '--sort', dest='sort', action='store_true', required=False, default=False, help='Include to sort the rolls.')
    parser.add_argument('-db', '--debug', dest='debug', action='store_true', required=False, default=False, help='Include flag to see the values generated.')

    return parser



if __name__ == '__main__':

    parser = gen_parser()
    args = parser.parse_args()
    num_sides = args.number_sides
    side_weighted = args.side_weighted
    weight = args.weight
    num_dice = args.number_dice
    sort = args.sort
    debug = args.debug

    rolls = []
    for _ in range(num_dice):
        r, numbers = roll_die(num_sides, side_weighted, weight, debug)
        rolls.append(r)

    if sort == True:
        rolls = sorted(rolls, reverse=True)

    for i, r in enumerate(rolls):
        print("Die {}: {}".format(i+1, r))

    if debug:
        if side_weighted == None and weight == None:
            message = 'With no side weighted, the numbers chosen from are:\n{}'.format(sorted(numbers))

        else:
            message = 'With {} being rolled every 1/{} rolls, the numbers to choose from are \n{}\n'.format(side_weighted, weight, sorted(numbers))

        print(message)
