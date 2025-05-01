from window import Window
from drawing import Point, Line


def main():
    win = Window(800, 600)
    point1 = Point(1, 2)
    point2 = Point(400, 500)
    line1 = Line(point1, point2)
    win.draw_line(line1, "blue")
    win.wait_for_close()


main()