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
gif1 = PhotoImage(file = 'flag')
arena.create_image(500, 0, image = gif1, anchor = NE,)

#create triangle robot
arena.pack() 
arena.update_idletasks()



"""
run program
"""

for t in range(0,445): #loops 445 times
    arena.move(robot , 1 , 0) #moves the robot 1 pixel right
    arena.update() #updates the arena
    time.sleep(0.01) #sleeps 0.01 seconds

    


window.mainloop() 
