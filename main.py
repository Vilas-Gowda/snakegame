import ui
from ui import a 

run_game = ui.start_ui()

x = 4
y = 25

while run_game == 1:
    a[x][y] = '0'
    ui.clear()
    ui.output_ui()
    move = input("")
    if move.upper() == 'W':
        a[x][y] = ' '
        x = x-1
        ui.wallencounter(x,y)
        a[x][y] = 'O'
    elif move.upper() == 'S':
        a[x][y] = ' '
        x = x+1
        ui.wallencounter(x,y)
        a[x][y] = 'O'
    elif move.upper() == 'A':
        a[x][y] = ' '
        y = y-1
        ui.wallencounter(x,y)
        a[x][y] = 'O'
    elif move.upper() == 'D':
        a[x][y] = ' '
        y = y+1
        ui.wallencounter(x,y)
        a[x][y] = 'O'














