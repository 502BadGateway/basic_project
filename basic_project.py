"""
set up window
"""

from Tkinter import * # imports everything from the Tkinter library
window = Tk() # generates a window 
arena = Canvas(window, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
arena.pack()
key = Canvas(window, width = 500, height = 100, bg = 'grey') # generates a canvas for our key and UI area
key.pack()

"""
objects in arena
"""

obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red") # creates a obstacle to avoid
obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red")
obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red")
obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red")
obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red")
obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red")
start_area = arena.create_rectangle(0, 450, 50, 500, fill = "#00FF99") # uses a Hexidecimal code for light green
#flag gif
gif1 = PhotoImage(file = 'flag.gif')
arena.create_image(500, 0, image = gif1, anchor = NE)
#create triangle robot
arena.create_polygon([(1, 1), (1, 200), (100, 100)])
arena.pack()
arena.update_idletasks()
window.mainloop()


"""
run program
"""

window.mainloop() # runs everything
