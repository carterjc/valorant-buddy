import tkinter as tk
import random


def get_screen_res(t=None, m=1.0):
	# pass through h to get only the height of the monitor, m to modify
	# Returns geometry str: [width]x[height]+[left]+[top]

	root = tk.Tk()
	root.wm_attributes('-transparentcolor', 'black')  # makes sure there is no annoying temp popup
	root.update_idletasks()
	root.attributes('-fullscreen', True)
	root.state('iconic')
	geometry = root.winfo_geometry()
	root.destroy()
	if t == 'h':
		return int(int(geometry.split("+")[0].split("x")[1])*m)
	elif t == 'w':
		return int(int(geometry.split("+")[0].split("x")[0])*m)
	return geometry


ASSET_PATH = '.\\assets\\'

# buddy config
BUDDY_X_POS = get_screen_res('w', .85)
BUDDY_Y_POS = get_screen_res('h', .9)
CYCLE = 0
CHECK = 1
IDLE_NUM = [1, 2, 3, 4]
SLEEP_NUM = [10, 11, 12, 13, 15]
WALK_LEFT = [6, 7]
WALK_RIGHT = [8, 9]
EVENT_NUMBER = random.randrange(1, 3, 1)

# sign config
SIGN_X_POS = get_screen_res('w', .85)
SIGN_Y_POS = get_screen_res('h', .81)
