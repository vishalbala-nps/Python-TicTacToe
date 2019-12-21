from tkinter import *
from tkinter import messagebox

#Defining Variables
current_player=""
game_started=False
p1_name=""
p2_name=""
#Functions
def display_help():
    """
    messagebox.showinfo("Help", "This is a simple Tic Tac Toe Game. To start, enter the Names of the players and click on Start Game")
    """
    b0.configure(state='disabled')
def set_player():
    global current_player
    global info_label
    if current_player == "p1":
        current_player = "p2"
        info_label.config(text=p2_name+"'s turn")
    else:
        current_player = "p1"
        info_label.config(text=p1_name+"'s turn")

def start_stop():
    global game_started
    global p1_name, p2_name
    global p1_box, p2_box
    global info_label
    global current_player
    tname1 = p1_box.get()
    tname2 = p2_box.get()
    if game_started == False:
        if tname1 != "" and tname2 != "":
            p1_name = tname1
            p2_name = tname2
            game_started = True
            playstop_text.set("Stop Game")
            set_player()
    else:
        game_started = False
        p1_name = ""
        p2_name = ""
        current_player = ""
        p1_box.delete(0, END)
        p2_box.delete(0, END)
        info_label.config(text="Click Start Game to start playing!")
        playstop_text.set("Start Game")



#Main program starts here
#Configuring the UI
window = Tk()
window.title("Tic-Tac Toe")
window.geometry("565x635")

label = Label(text="Player 1:", font=("Helvetica", 16))
label.grid(row=1, column=0)

p1_box = Entry()
p1_box.grid(row=1, column=1)

playstop_text = StringVar()
playstop = Button(window, textvariable=playstop_text, width=10, command=start_stop)
playstop_text.set("Start Game")
playstop.grid(row = 1, column = 2) 

label = Label(text="Player 2:", font=("Helvetica", 16))
label.grid(row=2, column=0)

p2_box = Entry()
p2_box.grid(row=2, column=1)

help = Button(window, text='Help', width=10, command=display_help)
help.grid(row = 2, column = 2)

info_label = Label(text="Click Start Game to start playing!", font=("Helvetica", 16))
info_label.grid(row=3, columnspan=3)


b0 = Button(window, text='hi', width=20, height=10)
b0.grid(row = 4, column = 0) 

b1 = Button(window, text='', width=20, height=10) 
b1.grid(row = 4, column = 1) 

b2 = Button(window, text='', width=20, height=10) 
b2.grid(row = 4, column = 2)

b3 = Button(window, text='', width=20, height=10)
b3.grid(row = 5, column = 0) 

b4 = Button(window, text='', width=20, height=10) 
b4.grid(row = 5, column = 1) 

b5 = Button(window, text='', width=20, height=10) 
b5.grid(row = 5, column = 2)

b6 = Button(window, text='', width=20, height=10) 
b6.grid(row = 6, column = 0) 

b7 = Button(window, text='', width=20, height=10) 
b7.grid(row = 6, column = 1) 

b8 = Button(window, text='', width=20, height=10) 
b8.grid(row = 6, column = 2) 


window.mainloop()