import tkinter as tk
from point import Point
from line import Line

class Window:
	def __init__(self, width: int, height: int, bg_color: str):
		self.width = width
		self.height = height
		self.__root = tk.Tk()
		self.__root.geometry(f"{self.width}x{self.height}")
		self.__root.title("Maze Solver")
		self.bg_color = "white"
		self.__canvas = tk.Canvas(self.__root, bg=self.bg_color, height=self.height, width=self.width)
		# fill: Stretch the content both horizontally and vertically
		# expand: Specifies whether the content should be expanded to consume extra space in their container
		self.__canvas.pack(fill=tk.BOTH, expand=True)
		self.__running = False
		# Set callback function for closing window
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		
	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()
		
	def wait_for_close(self):
		self.__running = True
		while self.__running:
			self.redraw()
		print("Closing")
			
	def close(self):
		self.__running = False
		
	def draw_line(self, line: Line, fill_color: str):
		line.draw(self.__canvas, fill_color)
		
	