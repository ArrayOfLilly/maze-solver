import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
	def test_maze_create_cells(self):
		win = Window(800, 600, "white")
		num_cols = 5
		num_rows = 5
		m1 = Maze(win, num_rows, num_cols, 100, 100)
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
		m2 = Maze(win, num_rows, num_cols, 100, 100)
		m2.break_entrance_and_exit()
		self.assertEqual(
			m2._cells[0][0].has_top_wall,
			0,
		)
		self.assertEqual(
			m2._cells[-1][-1].has_bottom_wall,
			0,
		)

	def test_reset_cells(self):
		win = Window(800, 600, "white")
		num_cols = 5
		num_rows = 5
		m3 = Maze(win, num_rows, num_cols, 100, 100)
		m3.break_entrance_and_exit()
		m3.break_walls()
		
		for i in range(num_rows):
			for j in range(num_cols):
				self.assertEqual(
					m3._cells[i][j].visited,
					False,
				)
		
		
if __name__ == "__main__":
	unittest.main()
