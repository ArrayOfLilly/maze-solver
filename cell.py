from line import Line
from point import Point
from window import Rectangle
from window import Window


class Cell:
	def __init__(self,
	             window: Window,
	             top_left_corner: Point,
	             bottom_right_corner: Point,
	             walls=(1, 1, 1, 1)
	             ):
		self.has_top_wall = walls[0]
		self.has_right_wall = walls[1]
		self.has_bottom_wall = walls[2]
		self.has_left_wall = walls[3]
		# for later use, now I center the maze
		self._top_left_x = top_left_corner.x
		self._top_left_y = top_left_corner.y
		self._bottom_right_x = bottom_right_corner.x
		self._bottom_right_y = bottom_right_corner.y
		self._win = window
		self.visited = False
		self.i = None
		self.j = None
	
	def draw_walls(self, fill_color: str):
		if self._win is None:
			return
		
		if self.has_top_wall:
			self._win.draw_line(self._get_top_wall(), fill_color)
		if self.has_right_wall:
			self._win.draw_line(self._get_right_wall(), fill_color)
		if self.has_bottom_wall:
			self._win.draw_line(self._get_bottom_wall(), fill_color)
		if self.has_left_wall:
			self._win.draw_line(self._get_left_wall(), fill_color)
			
	def draw(self, fill_color: str, bg_color="white smoke"):
		if self._win is None:
			return
		
		self._win.draw_rectangle(Rectangle(Point(self._top_left_x, self._top_left_y),
		                                   Point(self._bottom_right_x, self._bottom_right_y)),
		                         fill_color=bg_color)
		if not self.has_top_wall:
			self._win.draw_line(self._get_top_wall(), bg_color)
		if not self.has_right_wall:
			self._win.draw_line(self._get_right_wall(), bg_color)
		if not self.has_bottom_wall:
			self._win.draw_line(self._get_bottom_wall(), bg_color)
		if not self.has_left_wall:
			self._win.draw_line(self._get_left_wall(), bg_color)
			
		self.draw_walls(fill_color)
		
	def _get_top_wall(self):
		x = Point(self._top_left_x, self._top_left_y)
		y = Point(self._bottom_right_x, self._top_left_y)
		line = Line(x, y)
		return line
	
	def _get_right_wall(self):
		x = Point(self._bottom_right_x, self._top_left_y)
		y = Point(self._bottom_right_x, self._bottom_right_y)
		line = Line(x, y)
		return line
	
	def _get_bottom_wall(self):
		x = Point(self._top_left_x, self._bottom_right_y)
		y = Point(self._bottom_right_x, self._bottom_right_y)
		line = Line(x, y)
		return line
	
	def _get_left_wall(self):
		x = Point(self._top_left_x, self._top_left_y)
		y = Point(self._top_left_x, self._bottom_right_y)
		line = Line(x, y)
		return line
	
	def draw_move(self, to_cell, undo=False):
		if self._win is None:
			return
		from_cell = self.get_center()
		to_cell = to_cell.get_center()
		line = Line(from_cell, to_cell)
		if undo:
			fill_color = "grey82"
			width = 2
		else:
			fill_color = "OrangeRed2"
			width = 3
		self._win.draw_line(line, fill_color, width)
	
	def get_center(self):
		x = (self._top_left_x + self._bottom_right_x) / 2
		y = (self._top_left_y + self._bottom_right_y) / 2
		center = Point(x, y)
		return center
	
	def set_wall(self, walls):
		self.has_top_wall = walls[0]
		self.has_right_wall = walls[1]
		self.has_bottom_wall = walls[2]
		self.has_left_wall = walls[3]
	
	
		