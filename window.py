import tkinter as tk


class Window:
	def __init__(self, width, height):
		self.__root = tk.Tk()
		# self.__root.geometry(f"{width}x{height}")
		self.__root.title("Maze Solver")
		self.__c = tk.Canvas(self.__root, bg="white", height=height, width=width)
		# fill: Stretch the content both horizontally and vertically
		# expand: Specifies whether the content should be expanded to consume extra space in their container
		self.__c.pack(fill=tk.BOTH, expand=True)
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
		

