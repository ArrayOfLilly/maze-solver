from point import Point
from line import Line
from window import Window
from cell import Cell
from maze import Maze


def main():
	win = Window(800, 600)
	
	#top_left_corner = Point(100, 100)
	# bottom_right_corner = Point(200, 200)
	# cell = Cell(win, top_left_corner, bottom_right_corner, (1, 0, 1, 0))
	# cell.draw("red4")
	#
	# top_left_corner2 = Point(200, 100)
	# bottom_right_corner2 = Point(300, 200)
	# cell2 = Cell(win, top_left_corner2, bottom_right_corner2, (1, 1, 0, 0))
	# cell2.draw("red4")
	#
	# top_left_corner3 = Point(200, 200)
	# bottom_right_corner3 = Point(300, 300)
	# cell3 = Cell(win, top_left_corner3, bottom_right_corner3, (0, 1, 0, 1))
	# cell3.draw("red4")
	#
	# cell.draw_move(cell2, False)
	# cell2.draw_move(cell3, True)
	
	top_left_corner = Point(100, 100)
	maze = Maze(win, top_left_corner, 3, 3,100, 100)
	
	win.wait_for_close()
	
	
main()

