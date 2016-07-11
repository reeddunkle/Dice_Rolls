# Roll Dice

A simple script to roll dice. The user specifies the number of dice to roll, how many side are on the dice, and can optionally weight the dice on a side, and specify the weighted probability.

Installation
----

Clone the repo:

```
git clone
```

Navigate to the repo

```
cd Dice_Rolls
```

Roll Dice from the Command Line
----

For a standard die roll, run the script followed by a number to specify how many sides.
For example, this rolls a 6-sided die:

```
python roll_dice.py 6
```

To roll multiple dice, use the --dice (`-d`) flag and specify how many dice:

```
python roll_dice.py 6 -d 2
```

To weigh the dice, use the --weigh (`-w`) flag and specify which side to weigh, and the --prob (`-p` or `1/`) flag to specify the probability of that side being rolled (1/x times that number will be rolled):

```
python roll_dice.py 6 --weigh 5 -p 2  # 1 out of 2 times, a 5 will be rolled
```

To sort the rolls from highest to lowest, include the `--sort` (`-s`) flag:

```
python rolle_dice.py 6 -d 5 --sort

# Die 1: 5
# Die 2: 5
# Die 3: 4
# Die 4: 3
# Die 5: 2
```

To run debugging mode, iinclude the --debug (`-db`) flag and the list of numbers the roll is chosen from will be displayed:

```
python roll_dice.py 6 -w 6 -p 2 -db
```

Create a set of Dice objects
----

Let's say that you're playing D&D, and you need five 20-sided dice.

- From the root directory, start a python repl by simply typing `python` into the command line.
- Import the Dice object from the module:

```
from roll_dice import Dice
```

- Create your five dice (optional--setting `sort=True` will display the rolls highest to lowest):

```
dice = Dice(sides=20, num_dice=5, sort=True)
```

- Roll them:

```
dice.roll()

# Die 1: 20
# Die 2: 16
# Die 3: 13
# Die 4: 6
# Die 5: 2
```

Create weighted dice
----

An example of weighted dice:

```
dice = Dice(sides=6, side_weighted=6, weight=2, num_dice=5)
dice.roll()

# Die 1: 3
# Die 2: 4
# Die 3: 3
# Die 4: 6
# Die 5: 6
```
