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

Roll Dice!
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

To run debugging mode, set the --debug (`-db`) flag to `True`, and the list of numbers the roll is chosen from will be displayed:

```
python roll_dice.py 6 -w 6 -p 2 -db True
```
