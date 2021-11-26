import random
import tkinter as tk
from PIL import ImageTk, Image
import valorant

import config


# transfer random no. to event
def event(cycle, check, event_number, x, y):
	if event_number in config.IDLE_NUM:
		check = 0
		bwindow.after(400, update_buddy, cycle, check, event_number, x, y)  # no. 1,2,3,4 = idle
	elif event_number == 5:
		check = 1
		bwindow.after(100, update_buddy, cycle, check, event_number, x, y)  # no. 5 = idle to sleep
	elif event_number in config.WALK_LEFT:
		check = 4
		bwindow.after(100, update_buddy, cycle, check, event_number, x, y)  # no. 6,7 = walk towards left
	elif event_number in config.WALK_RIGHT:
		check = 5
		bwindow.after(100, update_buddy, cycle, check, event_number, x, y)  # no 8,9 = walk towards right
	elif event_number in config.SLEEP_NUM:
		check = 2
		bwindow.after(1000, update_buddy, cycle, check, event_number, x, y)  # no. 10,11,12,13,15 = sleep
	elif event_number == 14:
		check = 3
		bwindow.after(100, update_buddy, cycle, check, event_number, x, y)  # no. 15 = sleep to idle


# making gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
	if cycle < len(frames) - 1:
		cycle += 1
	else:
		cycle = 0
		event_number = random.randrange(first_num, last_num + 1, 1)
	return cycle, event_number


def update_buddy(cycle, check, event_number, x, y):
	# idle
	if check == 0:
		frame = idle[cycle]
		cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

	# idle to sleep
	elif check == 1:
		frame = idle_to_sleep[cycle]
		cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
	# sleep
	elif check == 2:
		frame = sleep[cycle]
		cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
	# sleep to idle
	elif check == 3:
		frame = sleep_to_idle[cycle]
		cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
	# walk toward left
	elif check == 4:
		frame = walk_positive[cycle]
		cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
		x -= 3
	# walk towards right
	elif check == 5:
		frame = walk_negative[cycle]
		cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
		x -= -3
	bwindow.geometry('100x100+' + str(x) + "+" + str(y))
	label.configure(image=frame)
	bwindow.after(1, event, cycle, check, event_number, x, y)


def check_val_connection():
	try:
		client = valorant.LocalClient()
		client.get_session()['loaded']
		return "valorant >:)"
	except:
		return "no valorant :("


def update_sign():
	v.set(check_val_connection())
	twindow.after(1, update_sign)


bwindow = tk.Tk()

# creates gif references

# idle gif
idle = [tk.PhotoImage(
	file=config.ASSET_PATH + 'idle.gif',
	format='gif -index %i' % i) for i in range(5)
]
# idle to sleep gif
idle_to_sleep = [
	tk.PhotoImage(
		file=config.ASSET_PATH + 'idle_to_sleep.gif',
		format='gif -index %i' % i) for i in range(8)
]
# sleep gif
sleep = [
	tk.PhotoImage(
		file=config.ASSET_PATH + 'sleep.gif',
		format='gif -index %i' % i) for i in range(3)
]
# sleep to idle gif
sleep_to_idle = [
	tk.PhotoImage(
		file=config.ASSET_PATH + 'sleep_to_idle.gif',
		format='gif -index %i' % i) for i in range(8)
]
# walk to left gif
walk_positive = [
	tk.PhotoImage(
		file=config.ASSET_PATH + 'walking_left.gif',
		format='gif -index %i' % i) for i in range(8)
]
# walk to right gif
walk_negative = [
	tk.PhotoImage(
		file=config.ASSET_PATH + 'walking_right.gif',
		format='gif -index %i' % i) for i in range(8)
]

# sign
twindow = tk.Toplevel()
twindow.geometry("300x236+" + str(config.SIGN_X_POS) + "+" + str(config.SIGN_Y_POS))
img = ImageTk.PhotoImage(Image.open(config.ASSET_PATH + "wood_sign.png"))
v = tk.StringVar()
v.set(check_val_connection())
sign = tk.Label(twindow, textvariable=v, image=img, compound='center').pack()


twindow.overrideredirect(True)
twindow.wm_attributes('-transparentcolor', 'white')
twindow.after(20000, update_sign)  # 20 seconds

# window configuration
bwindow.config(highlightbackground='black')
label = tk.Label(bwindow, bd=0, bg='black')
bwindow.overrideredirect(True)
bwindow.wm_attributes('-transparentcolor', 'black')
label.pack()
# loop the program
bwindow.after(1, update_buddy, config.CYCLE, config.CHECK, config.EVENT_NUMBER, config.BUDDY_X_POS, config.BUDDY_Y_POS)
bwindow.mainloop()
