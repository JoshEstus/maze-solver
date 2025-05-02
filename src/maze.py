import time

from drawing import Cell

class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.window))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.window is None:
            return
        x1 = self.x1 + (j * self.cell_size_x)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (i * self.cell_size_y)
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, x2, y1, y2)
        self._animate()


    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        top_left = self.cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0,0)
        bottom_right = self.cells[-1][-1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self.num_cols -1, self.num_rows - 1)