from maze import Maze
from window import Window


def main():
	win = Window(800, 600, "gold")
	
	maze = Maze(win, 12, 18, 40, 40)
	maze.break_entrance_and_exit()
	maze.break_walls()
	
	win.wait_for_close()


main()
