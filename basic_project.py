from Tkinter import*
window = Tk()
arena = Canvas(window, width = 500, height = 500, bg = 'white')
arena.pack()
key = Canvas(window, width = 500, height = 100, bg = 'grey')
key.pack()
objectrectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red")
objectrectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red")
objectrectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red")
objectrectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red")
objectrectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red")
objectrectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red")
objectrectangle7 = arena.create_rectangle(0, 450, 50, 500, fill = "#00FF99")

window.mainloop()

