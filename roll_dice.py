'''
    roll_dice
    ~~~~~~~~~

    Roll a die. Optionally weigh the die, and specify the weight.
'''



import random
import argparse



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
        dist = num_sides - 1
        numbers = sum([[n] * (weight-1) + [side_weighted] for n in range(1, num_sides+1) if n is not side_weighted], [])


    roll = random.choice(numbers)

    return (roll, numbers)


def gen_parser():
    '''
    Creates command-line parser to access dice values.
    '''

    parser = argparse.ArgumentParser(description='Roll a die')
    parser.add_argument('number_sides', type=int, help='Number of sides the die has.')
    parser.add_argument('-d', '--dice', dest='number_dice', required=False, nargs='?', default=1, type=int, help='Number of dice to roll.')
    parser.add_argument('-w', '--weigh', dest='side_weighted', required=False, nargs='?', default=None, type=int, help='Weigh the die for this side.')
    parser.add_argument('-p', '-1/', '--prob', dest='weight', required=False, nargs='?', default=None, type=int, help='The probability the weighed side will be rolled. 1/x rolls will be the weighted roll.')
    parser.add_argument('-db', '--debug', dest='debug', required=False, nargs='?', default=False, type=bool, help='Set to True to see the values generated.')

    return parser



if __name__ == '__main__':

    parser = gen_parser()
    args = parser.parse_args()
    num_sides = args.number_sides
    side_weighted = args.side_weighted
    weight = args.weight
    debug = args.debug

    num_dice = args.number_dice

    for _ in range(num_dice):
        roll, numbers = roll_die(num_sides, side_weighted, weight, debug)
        print(roll)

    if debug:
        print('With {} being rolled every 1/{} rolls, the numbers to choose from are \n{}\n'.format(side_weighted, weight, sorted(numbers)))
