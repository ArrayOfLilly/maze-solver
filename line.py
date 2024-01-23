import tkinter as tk

from point import Point


class Line:
	def __init__(self, start: Point, end: Point):
		self.start = start
		self.end = end
	
	def draw(self, canvas: tk.Canvas, fill_color: str, width=3):
		canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=width)
		canvas.pack(fill=tk.BOTH, expand=True)
