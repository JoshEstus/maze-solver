import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_with_more_cols(self):
        num_cols = 200
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_with_more_col_length(self):
        num_cols = 200
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 100)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 50)
        top_left = m1.cells[0][0]
        self.assertEqual(top_left.has_top_wall, False)
        bottom_right = m1.cells[-1][-1]
        self.assertEqual(bottom_right.has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()