import functions
from functions import a
import random

run_game = functions.start_ui()

x = 7
y = 25

while run_game == 1:
    a[x][y] = '0'
    functions.clear()
    functions.output_ui()
    move = input("")
    if move.upper() == 'W':
        a[x][y] = ' '
        x = x-1
        a[x][y] = 'O'
    elif move.upper() == 'S':
        a[x][y] = ' '
        x = x+1
        a[x][y] = 'O'
    elif move.upper() == 'A':
        a[x][y] = ' '
        y = y-1
        a[x][y] = 'O'
    elif move.upper() == 'D':
        a[x][y] = ' '
        y = y+1
        a[x][y] = 'O'
    














