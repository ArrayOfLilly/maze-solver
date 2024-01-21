from point import Point
import tkinter as tk


class Line:
	def __init__(self, start: Point, end: Point):
		self.start = start
		self.end = end
	
	def draw(self, canvas: tk.Canvas, fill_color: str):
		canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
		canvas.pack(fill=tk.BOTH, expand=True)
