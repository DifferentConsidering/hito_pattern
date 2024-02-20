from graphics import Window
from pattern import Pattern
import sys


def main():
    row_nums = [0,1,1,0,1,1,1,0,1,0,0,1]
    col_nums = [0,1,1,1,1,0,1,0,0,1,1,0,0,1]
    margin = 50
    screen_x = 800
    screen_y = 600
    

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    pattern = Pattern()
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()