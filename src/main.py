from window import Window
from drawing import Point, Line, Cell


def main():
    win = Window(800, 600)
    point1 = Point(350, 450)
    point2 = Point(400, 500)
    cell = Cell(win)
    cell.has_bottom_wall = True
    cell.has_top_wall = False
    cell.has_left_wall = False
    cell.draw(point1.x, point2.x, point1.y, point2.y)
    win.wait_for_close()


main()