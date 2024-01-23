import random
from time import sleep

from cell import Cell
from point import Point
from window import Window


class Maze:
	def __init__(self,
	             window: Window,
	             num_rows: int,
	             num_columns: int,
	             cell_size_x=50,
	             cell_size_y=50,
	             seed=0,
	             fill_color="grey19",
	             top_left_corner=Point(0, 0)
	             ):
		# later use, now I draw centered
		self.x1 = top_left_corner.x
		self.y1 = top_left_corner.y
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self._win = window
		self.seed = seed
		random.seed(self.seed)
		self.fill_color = fill_color
		self._cells = []
		self._create_cells()
	
	def _create_cells(self):
		
		if self.num_rows * self.cell_size_y > self._win.height or self.num_columns * self.cell_size_x > self._win.width:
			return
		
		rows = []
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
				cell.draw(self.fill_color)
				self._animate(0.05)
	
	def _animate(self, time):
		sleep(time)
		self._win.redraw()
	
	def break_entrance_and_exit(self):
		entrance = self._cells[0][0]
		maze_exit = self._cells[-1][-1]
		
		entrance.set_wall((0, 1, 1, 1))
		maze_exit.set_wall((1, 1, 0, 1))
		
		entrance.draw(self.fill_color)
		self._animate(1.2)
		maze_exit.draw(self.fill_color)
		self._animate(1.2)
	
	def _retouch(self):
		for row in self._cells:
			for cell in row:
				cell.draw_walls(self.fill_color)
	
	def _reset_cells_visited(self):
		for row in self._cells:
			for cell in row:
				cell.visited = False

	def break_walls(self):
		self.break_walls_r(0, 0)
		self._retouch()
		self._reset_cells_visited()
	
	def break_walls_r(self, i, j):
		self._cells[i][j].visited = True
		while True:
			possible_directions = []
			if j > 0 and not self._cells[i][j - 1].visited:
				possible_directions.append("left")
			if j < self.num_columns - 1 and not self._cells[i][j + 1].visited:
				possible_directions.append("right")
			if i > 0 and not self._cells[i - 1][j].visited:
				possible_directions.append("up")
			if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
				possible_directions.append("down")
			
			if len(possible_directions) == 0:
				self._cells[i][j].draw(self.fill_color)
				self._animate(0.05)
				return
			
			direction = random.choice(possible_directions)
			if direction == "left":
				# print(f"Left from: cells[{i}][{j}]")
				self._cells[i][j].has_left_wall = False
				self._cells[i][j - 1].has_right_wall = False
				self.break_walls_r(i, j - 1)
			elif direction == "right":
				# print(f"Right from: cells[{i}][{j}]")
				self._cells[i][j].has_right_wall = False
				self._cells[i][j + 1].has_left_wall = False
				self.break_walls_r(i, j + 1)
			elif direction == "up":
				# print(f"Up from: cells[{i}][{j}]")
				self._cells[i][j].has_top_wall = False
				self._cells[i - 1][j].has_bottom_wall = False
				self.break_walls_r(i - 1, j)
			elif direction == "down":
				# print(f"Down from: cells[{i}][{j}]")
				self._cells[i][j].has_bottom_wall = False
				self._cells[i + 1][j].has_top_wall = False
				self.break_walls_r(i + 1, j)
			
			