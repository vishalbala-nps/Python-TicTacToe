from tkinter import *

#Defining Variables
current_player="p1"

#Configuring the UI
window = Tk()
window.title("Tic-Tac Toe")
window.geometry("625x625")

label = Label(text="Player 1:", font=("Helvetica", 16))
label.grid(row=1, column=0)

p1_name = Entry()
p1_name.grid(row=1, column=1)

play = Button(window, text='Start Game', width=10)
play.grid(row = 1, column = 2) 

label = Label(text="Player 2:", font=("Helvetica", 16))
label.grid(row=2, column=0)

p2_name = Entry()
p2_name.grid(row=2, column=1)

help = Button(window, text='Help', width=10)
help.grid(row = 2, column = 2)

label = Label(text="Player 1 to play", font=("Helvetica", 16))
label.grid(row=3, column=1)

b0 = Button(window, text='Hi', width=20, height=10)
b0.grid(row = 4, column = 0) 

b1 = Button(window, text='Hi', width=20, height=10) 
b1.grid(row = 4, column = 1) 

b2 = Button(window, text='Hi', width=20, height=10) 
b2.grid(row = 4, column = 2)

b3 = Button(window, text='Hi', width=20, height=10)
b3.grid(row = 5, column = 0) 

b4 = Button(window, text='Hi', width=20, height=10) 
b4.grid(row = 5, column = 1) 

b5 = Button(window, text='Hi', width=20, height=10) 
b5.grid(row = 5, column = 2)

b6 = Button(window, text='Hi', width=20, height=10) 
b6.grid(row = 6, column = 0) 

b7 = Button(window, text='Hi', width=20, height=10) 
b7.grid(row = 6, column = 1) 

b8 = Button(window, text='Hi', width=20, height=10) 
b8.grid(row = 6, column = 2) 


window.mainloop()