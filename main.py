from maze import Maze
from window import Window


def main():
	win = Window(800, 600, "gold")
	
	maze = Maze(win, 9, 12, 50, 50)
	maze.break_entrance_and_exit()
	maze.break_walls()
	maze.solve()
	
	win.wait_for_close()


main()
