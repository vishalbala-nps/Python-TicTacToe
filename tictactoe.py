from tkinter import *
from tkinter import messagebox

#Defining Variables
current_player=""
game_started=False
p1_name=""
p2_name=""
b_status = ["","","","","","","","",""]
#Functions
def display_help():
    messagebox.showinfo("Help", "This is a simple Tic Tac Toe Game. To start, enter the Names of the players and click on Start Game")

def boxes_config(state1):
    b0.config(text="", state=state1)
    b1.config(text="", state=state1)
    b2.config(text="", state=state1)
    b3.config(text="", state=state1)
    b4.config(text="", state=state1)
    b5.config(text="", state=state1)
    b6.config(text="", state=state1)
    b7.config(text="", state=state1)
    b8.config(text="", state=state1)

def set_player():
    global current_player
    global info_label
    if current_player == "p1":
        current_player = "p2"
        info_label.config(text=p2_name+"'s turn")
    else:
        current_player = "p1"
        info_label.config(text=p1_name+"'s turn")

def stopgame():
    global game_started
    global p1_name, p2_name
    global p1_box, p2_box
    global info_label
    global current_player
    global b_status
    p1_box.config(state='normal')
    p2_box.config(state='normal')
    p1_name = ""
    p2_name = ""
    current_player = ""
    b_status = ["","","","","","","","",""]
    game_started=False
    p1_box.delete(0, END)
    p2_box.delete(0, END)
    info_label.config(text="Click Start Game to start playing!")
    boxes_config("disabled")
    playstop_text.set("Start Game")

def start_stop():
    global game_started
    global p1_name, p2_name
    global p1_box, p2_box
    global info_label
    global current_player
    global b_status
    tname1 = p1_box.get()
    tname2 = p2_box.get()
    if game_started == False:
        if tname1 != "" and tname2 != "":
            p1_box.config(state='disabled')
            p2_box.config(state='disabled')
            p1_name = tname1
            p2_name = tname2
            game_started = True
            playstop_text.set("Stop Game")
            set_player()
            boxes_config("active")
    else:
        stopgame()

def isGameover():
    if checkWinner() != True:
        for i in b_status:
            print(i)
            if i == "":
                return False
        return True
    else:
        return False

def checkWinner():
    if b_status[0] == "p1" and b_status[1] == "p1" and b_status[2] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[0] == "p2" and b_status[1] == "p2" and b_status[2] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[3] == "p1" and b_status[4] == "p1" and b_status[5] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[3] == "p2" and b_status[4] == "p2" and b_status[5] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[6] == "p1" and b_status[7] == "p1" and b_status[8] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[6] == "p2" and b_status[7] == "p2" and b_status[8] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[0] == "p1" and b_status[3] == "p1" and b_status[6] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[0] == "p2" and b_status[3] == "p2" and b_status[6] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[1] == "p1" and b_status[4] == "p1" and b_status[7] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[1] == "p2" and b_status[4] == "p2" and b_status[7] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[2] == "p1" and b_status[5] == "p1" and b_status[8] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[2] == "p2" and b_status[5] == "p2" and b_status[8] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[0] == "p1" and b_status[4] == "p1" and b_status[8] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[0] == "p2" and b_status[4] == "p2" and b_status[8] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    elif b_status[2] == "p1" and b_status[4] == "p1" and b_status[6] == "p1":
        messagebox.showinfo("Game Over", "Game Over "+p1_name+" is the winner")
        stopgame()
        return True
    elif b_status[2] == "p2" and b_status[4] == "p2" and b_status[6] == "p2":
        messagebox.showinfo("Game Over", "Game Over "+p2_name+" is the winner")
        stopgame()
        return True
    else:
        return False



def b0_click():
    global b0
    global b_status
    bval = 0
    if current_player == "p1":
        b_status[bval] = "p1"
        b0.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b0.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")
        stopgame()


def b1_click():
    global b1
    global b_status
    bval = 1
    if current_player == "p1":
        b_status[bval] = "p1"
        b1.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b1.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b2_click():
    global b2
    global b_status
    bval = 2
    if current_player == "p1":
        b_status[bval] = "p1"
        b2.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b2.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b3_click():
    global b0
    global b_status
    bval = 3
    if current_player == "p1":
        b_status[bval] = "p1"
        b3.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b3.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b4_click():
    global b4
    global b_status
    bval = 4
    if current_player == "p1":
        b_status[bval] = "p1"
        b4.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b4.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b5_click():
    global b5
    global b_status
    bval = 5
    if current_player == "p1":
        b_status[bval] = "p1"
        b5.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b5.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")
        
def b6_click():
    global b6
    global b_status
    bval = 6
    if current_player == "p1":
        b_status[bval] = "p1"
        b6.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b6.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b7_click():
    global b7
    global b_status
    bval = 7
    if current_player == "p1":
        b_status[bval] = "p1"
        b7.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b7.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

def b8_click():
    global b8
    global b_status
    bval = 8
    if current_player == "p1":
        b_status[bval] = "p1"
        b8.config(text="X", state='disabled')
    else:
        b_status[bval] = "p2"
        b8.config(text="O", state='disabled')
    set_player()
    if isGameover() == True:
        messagebox.showinfo("Game Over", "Game Over")

#Main program starts here
#Configuring the UI
window = Tk()
window.title("Tic-Tac Toe")
window.geometry("665x665")

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

b0 = Button(window, text='X', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b0_click)
b0.grid(row = 4, column = 0) 

b1 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b1_click) 
b1.grid(row = 4, column = 1) 

b2 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b2_click) 
b2.grid(row = 4, column = 2)

b3 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b3_click)
b3.grid(row = 5, column = 0) 

b4 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b4_click) 
b4.grid(row = 5, column = 1) 

b5 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b5_click) 
b5.grid(row = 5, column = 2)

b6 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b6_click) 
b6.grid(row = 6, column = 0) 

b7 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b7_click) 
b7.grid(row = 6, column = 1) 

b8 = Button(window, text='', width=15, height=6 ,font='Times 20 bold', disabledforeground="black", command=b8_click) 
b8.grid(row = 6, column = 2) 

boxes_config("disabled")

window.mainloop()