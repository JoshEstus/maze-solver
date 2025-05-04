from window import Window
from maze import Maze
import sys


def main():

    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(2000)

    num_rows = 40
    num_cols = 40
    margin = 10
    screen_x = 1200
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze Created...")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze cannot be solved!")
    else:
        print("Maze solved!")

    win.wait_for_close()


main()