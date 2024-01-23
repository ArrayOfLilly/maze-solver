import tkinter as tk

from point import Point


class Rectangle:
	def __init__(self, top_left_corner: Point, bottom_right_corner: Point, color="white smoke"):
		self.top_left = top_left_corner
		self.bottom_right = bottom_right_corner
		self.bg_color = color
	
	def draw(self, canvas: tk.Canvas, fill_color="white smoke"):
		canvas.create_rectangle(self.top_left.x, self.top_left.y,
		                        self.bottom_right.x, self.bottom_right.y,
		                        fill=fill_color)
		canvas.pack()
