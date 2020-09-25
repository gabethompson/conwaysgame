# conwaysgame
Python implementation of a randomly-generated Conway's Game of Life. It runs on command line and accepts arguments:

--size (int): Size of each side of the field on which it acts. Defaults to 100.

--ticklen (int): Length of each tick in the Game. Defaults to 50.

--rate (float): Portion of the board which begins alive. Defaults to 0.2, and will be 0.2 if the value is not between 0 and 1.

The board is continuous with itself - tiles on the right edge of the board will test tiles on the left edge of the board as if they were adjacent, and so on for the other edges of the board. (This results in a board which, if it were to be displayed in 3-dimensional space, would resemble a torus.)
