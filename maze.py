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
		self.__win = window
		self.__cells = []
		self._create_cells()
		
	def _create_cells(self):
		rows = []
		if self.num_rows * self.cell_size_y > self.__win.height \
				or self.num_columns * self.cell_size_x > self.__win.width:
			return
		maze_start_x = (self.__win.width - self.num_columns * self.cell_size_x) / 2
		maze_start_y = (self.__win.height - self.num_rows * self.cell_size_y) / 2
		
		for r in range(self.num_rows):
			columns = []
			for c in range(self.num_columns):
				start = Point(maze_start_x + c * self.cell_size_x, maze_start_y + r * self.cell_size_y)
				end = Point(maze_start_x + (c + 1) * self.cell_size_x, maze_start_y + (r + 1) * self.cell_size_y)
				cell = Cell(self.__win, start, end, (1, 1, 1, 1))
				columns.append(cell)
			rows.append(columns.copy())
		self.__cells = rows
		print(f"Rows: {len(self.__cells)}, columns: {len(self.__cells[0])}")
		self._draw_cells()
		
	def _draw_cells(self):
		count = 0
		for row in self.__cells:
			count += 1
			count1 = 0
			for cell in row:
				count1 += 1
				cell.draw("OrangeRed3")
				self._animate()
				
	def _animate(self):
		sleep(1)
		self.__win.redraw()
		