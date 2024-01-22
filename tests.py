import unittest
from point import Point
from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600, "white")
        num_cols = 5
        num_rows = 5
        p = Point(0, 0)
        m1 = Maze(win, p, num_rows, num_cols, 100, 100)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_has_entrance_and_exit(self):
        win = Window(800, 600, "white")
        num_cols = 3
        num_rows = 3
        p = Point(0, 0)
        m2 = Maze(win, p, num_rows, num_cols, 100, 100)
        m2.break_entrance_and_exit()
        self.assertEqual(
            m2._cells[0][0].has_top_wall,
            0,
        )
        self.assertEqual(
            m2._cells[-1][-1].has_bottom_wall,
            0,
        )

if __name__ == "__main__":
    unittest.main()