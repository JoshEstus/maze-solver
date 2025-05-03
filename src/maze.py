import time
import random

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
            window = None,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        if seed:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _reset_cells_visited(self):
        for col in self.cells:
            for row_cell in col:
                row_cell.visited = False

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
        time.sleep(.005)

    def _break_entrance_and_exit(self):
        top_left = self.cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0,0)
        bottom_right = self.cells[-1][-1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self.num_cols -1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            need_visit = []
            if i < self.num_cols -1  and not self.cells[i+1][j].visited:
                need_visit.append((i+1, j))

            if j < self.num_rows -1 and not self.cells[i][j+1].visited:
                need_visit.append((i, j+1))

            if i > 0 and not self.cells[i-1][j].visited:
                need_visit.append((i-1, j))

            if j > 0 and not self.cells[i][j-1].visited:
                need_visit.append((i, j-1))

            if len(need_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                ran_ind = random.randrange(0, len(need_visit))
                visiting = need_visit[ran_ind]
                if visiting[0] < i:
                    self.cells[visiting[0]][visiting[1]].has_bottom_wall = False
                    self.cells[i][j].has_top_wall = False
                if visiting[0] > i:
                    self.cells[visiting[0]][visiting[1]].has_top_wall = False
                    self.cells[i][j].has_bottom_wall = False
                if visiting[1] > j:
                    self.cells[visiting[0]][visiting[1]].has_left_wall = False
                    self.cells[i][j].has_right_wall = False
                if visiting[1] < j:
                    self.cells[visiting[0]][visiting[1]].has_right_wall = False
                    self.cells[i][j].has_left_wall = False
                self._break_walls_r(visiting[0], visiting[1])

    def solve(self):
        solved = self._solve_r(i=0,j=0)
        return solved


    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True

        if i == self.num_cols -1 and j == self.num_rows -1:
            return True

        if i > 0 and not self.cells[i][j].has_top_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            solved = self._solve_r(i-1, j)
            if solved:
                return solved
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], undo=True)

        if i < self.num_cols -1  and not self.cells[i][j].has_bottom_wall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            solved = self._solve_r(i+1, j)
            if solved:
                return solved
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j], undo=True)

        if j > 0  and not self.cells[i][j].has_left_wall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            solved = self._solve_r(i, j-1)
            if solved:
                return solved
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1], undo=True)

        if j < self.num_cols - 1 and not self.cells[i][j].has_right_wall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            solved = self._solve_r(i, j+1)
            if solved:
                return solved
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1], undo=True)

        return False
