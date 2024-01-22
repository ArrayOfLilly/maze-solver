from point import Point
from window import Window
from cell import Cell
from time import sleep


class Maze:
	def __init__(self,
	             window: Window,
	             top_left_corner: Point,
	             num_rows: int,
	             num_columns: int,
	             cell_size_x: int,
	             cell_size_y: int,
	             ):
		# later use, now I draw centered
		self.x1 = top_left_corner.x
		self.y1 = top_left_corner.y
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self._win = window
		self._cells = []
		self._create_cells()
		
	def _create_cells(self):
		rows = []
		if self.num_rows * self.cell_size_y > self._win.height \
				or self.num_columns * self.cell_size_x > self._win.width:
			return
		maze_start_x = (self._win.width - self.num_columns * self.cell_size_x) / 2
		maze_start_y = (self._win.height - self.num_rows * self.cell_size_y) / 2
		
		for r in range(self.num_rows):
			columns = []
			for c in range(self.num_columns):
				start = Point(maze_start_x + c * self.cell_size_x, maze_start_y + r * self.cell_size_y)
				end = Point(maze_start_x + (c + 1) * self.cell_size_x, maze_start_y + (r + 1) * self.cell_size_y)
				cell = Cell(self._win, start, end, (1, 1, 1, 1))
				columns.append(cell)
			rows.append(columns.copy())
		self._cells = rows
		self._draw_cells()
		
	def _draw_cells(self):
		for row in self._cells:
			for cell in row:
				cell.draw("OrangeRed3")
				self._animate(0.7)
				
	def _animate(self, time):
		sleep(time)
		self._win.redraw()
	
	def break_entrance_and_exit(self):
		entrance = self._cells[0][0]
		exit = self._cells[-1][-1]
		entrance.set_wall((0, 1, 1, 1))
		exit.set_wall((1, 1, 0, 1))
		entrance.draw("OrangeRed3")
		self._animate(1.2)
		exit.draw("OrangeRed3")
		self._animate(1.2)
		