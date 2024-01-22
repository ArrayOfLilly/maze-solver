from point import Point
from line import Line
from window import Window
from cell import Cell
from maze import Maze


def main():
	win = Window(800, 600, "white smoke")
	
	top_left_corner = Point(100, 100)
	maze = Maze(win, top_left_corner, 3, 3,100, 100)
	maze.break_entrance_and_exit()
	win.wait_for_close()
	
	
main()

