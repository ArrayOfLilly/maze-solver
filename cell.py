from point import Point
from line import Line
from window import Window


class Cell:
	def __init__(self, window: Window , top_left_corner: Point, bottom_right_corner: Point, walls=(1, 1, 1, 1)):
		self.has_top_wall = walls[0]
		self.has_right_wall = walls[1]
		self.has_bottom_wall = walls[2]
		self.has_left_wall = walls[3]
		self.__top_left_x = top_left_corner.x
		self.__top_left_y = top_left_corner.y
		self.__bottom_right_x = bottom_right_corner.x
		self.__bottom_right_y = bottom_right_corner.y
		self.__win = window
		
	def draw(self, fill_color: str):
		if self.has_top_wall:
			self.__win.draw_line(self.get_top_wall(), fill_color)
		if self.has_right_wall:
			self.__win.draw_line(self.get_right_wall(), fill_color)
		if self.has_bottom_wall:
			self.__win.draw_line(self.get_bottom_wall(), fill_color)
		if self.has_left_wall:
			self.__win.draw_line(self.get_left_wall(), fill_color)
		
	def get_top_wall(self):
		x = Point(self.__top_left_x, self.__top_left_y)
		y = Point(self.__bottom_right_x, self.__top_left_y)
		line = Line(x, y)
		return line
	
	def get_right_wall(self):
		x = Point(self.__bottom_right_x, self.__top_left_y)
		y = Point(self.__bottom_right_x, self.__bottom_right_y)
		line = Line(x, y)
		return line
	
	def get_bottom_wall(self):
		x = Point(self.__top_left_x, self.__bottom_right_y)
		y = Point(self.__bottom_right_x, self.__bottom_right_y)
		line = Line(x, y)
		return line
	
	def get_left_wall(self):
		x = Point(self.__top_left_x, self.__top_left_y)
		y = Point(self.__top_left_x, self.__bottom_right_y)
		line = Line(x, y)
		return line
	
	def draw_move(self, to_cell, undo=False):
		from_cell = self.get_center()
		to_cell = to_cell.get_center()
		line = Line(from_cell, to_cell)
		if undo:
			fill_color = "grey82"
		else:
			fill_color = "OrangeRed2"
		self.__win.draw_line(line, fill_color)
		
	def get_center(self):
		x = (self.__top_left_x + self.__bottom_right_x) / 2
		y = (self.__top_left_y + self.__bottom_right_y) / 2
		center = Point(x, y)
		return center
		