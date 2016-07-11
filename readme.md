# Roll Dice

A simple script to roll dice. The user specifies the number of dice to roll, how many side are on the dice, and can optionally weight the dice on a side, and specify the weighted probability.

Installation
----

Clone the repo:

```
git clone https://github.com/reeddunkle/Dice_Rolls
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

To sort the rolls from highest to lowest, include the `--sort` (`-s`) flag:

```
python rolle_dice.py 6 -d 5 --sort

# Die 1: 5
# Die 2: 5
# Die 3: 4
# Die 4: 3
# Die 5: 2
```

Add alias to roll from anywhere
----

**Create an alias in your `.bashrc` file**

Edit your file:

```
subl ~/.bashrc
```

At the bottom, or with your other aliases, add the following code. *Make sure that you add in the full path from your home (`~`) directory to the github repo. (Leave included the directory names that I have in the example path below.)*

```
# Roll dice from your terminal
alias roll="python ~/path/to/the/github_repo/Dice_Rolls/roll_dice.py"
```

Now you can type `roll`, and it will execute what is on the other side of the equals sign. This is equivalent to executing the script.

The two major advantages of doing this are:

1. You can be in any directory to execute this command. Without the alias, all of the executions you see below, when it says `python roll_dice.py ...` you have to be in the current directory to use it.

2. You don't have to tell it what script to execute (`roll_dice.py`) or with what program to interpret it (`python`).

**Note**: If at any time you move the directory to a different location, you'll have to update the path in the alias accordingly.

Examples (from anywhere in the terminal):

```
roll 6

# Die 1: 5

roll 20 -d 5 --sort

# Die 1: 11
# Die 2: 11
# Die 3: 10
# Die 4: 6
# Die 5: 1
```

Roll weighted dice
----

**Note**: If you created the alias above, you can substitute out the first part `python roll_dice.py` with `roll`

To roll weighted dice, use the --weigh (`-w`) flag and specify which side to weigh, and the --prob (`-p` or `1/`) flag to specify the probability of that side being rolled (1/x times that number will be rolled):

```
python roll_dice.py 6 --weigh 5 -p 2  # 1 out of 2 times, a 5 will be rolled
```

Debugging mode
----

To run debugging mode, include the --debug (`-db`) flag and the list of numbers from which the roll is chosen will be displayed:

```
python roll_dice.py 6 -w 6 -p 2 -db
```

Create a set of Dice objects in your code
----

Let's say that you're playing D&D, and you need five 20-sided dice.

- Navigate to the directory (`cd Dice_Rolls`)
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
