from os import system,name

def start_ui():
    print("Welcome to the Snake game!".center(100))
    print("1.start".center(100))
    print("2.exit ".center(100))
    run_game = int(input(""))
    while run_game >2 or run_game<1:
        run_game = input("Invalid input choose btw 1 or 2")

    if run_game == 2:
        clear()
        print("Thanks for playing!".center(100,'-'))
        exit()
    return run_game


def clear():
    if name == 'nt':
        _ = system('cls')   
    else:
        _ = system('clear')


clear()
a = [[' ' for i in range(100)] for j in range(20)]
def output_ui():
    for i in a:
        for j in i:
            print(j , end = '')
        print('\n')


