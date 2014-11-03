"""
set up window
"""
import time # Importing time library
from Tkinter import * # imports everything from the Tkinter library
window = Tk() # generates a window 
arena = Canvas(window, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
arena.pack()
key = Canvas(window, width = 500, height = 100, bg = 'grey') # generates a canvas for our key and UI area
key.pack()

"""
objects in arena
"""

obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red", outline = "red") # creates a obstacle to avoid
obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red", outline = "red")
obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red", outline = "red")
obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red", outline = "red")
obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red", outline = "red")
obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red", outline = "red")
start_area = arena.create_rectangle(0, 450, 50, 500, fill = "#82FA02") # uses a Hexidecimal code for light green

#flag gif
gif1 = PhotoImage(file = 'flag.gif')
arena.create_image(500, 0, image = gif1, anchor = NE,)

#create triangle robot
#robot = arena.create_polygon([(10, 450), (10, 500), (40, 475)], fill="#366605")
robot = arena.create_oval(50, 500, 30, 480, outline="green", fill="green", width=1)
arena.pack()
arena.update_idletasks()

"""
run program
"""

for t in range(0,450):
    arena.move(robot , 1 , 0)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0 , -0.335)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , -0.8 , 0)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0 , -0.4)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0.42 , 0)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0 , 0.155)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0.35 , 0)
    arena.update()
    time.sleep(0.001)
for t in range(0,450):
    arena.move(robot , 0 , -0.45)
    arena.update()
    time.sleep(0.001)
print robot (fill = 'red')
#robot_front, robot_back1, robot_back2 = arena.coords(robot)

#print robot_front


window.mainloop() # runs everything
