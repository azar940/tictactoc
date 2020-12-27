from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Tic Tac Toy By Aziz (update)")
imgx = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\png\001-cancel.png")
imgo = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\png\002-o.png")
imgf = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\png\free.png")
img1 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\png\1.png")
img2 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\png\2.png")
window.geometry("400x400")
window.columnconfigure([0, 1, 2], weight=3)
window.rowconfigure([0, 1, 2, 3], weight=3)
#
#
ActivePlayer = 1 #x
p1 = []
p2 = []
#
#
def setLoyet(id,img):
    if id == 1:
        but1.config(image=img, bg='#EB5555')
        but1["state"] = DISABLED
    if id == 2:
        but2.config(image=img, bg='#EB5555')
        but2["state"] = DISABLED
    if id == 3:
        but3.config(image=img, bg='#EB5555')
        but3["state"] = DISABLED
    if id == 4:
        but4.config(image=img, bg='#D33333')
        but4["state"] = DISABLED
    if id == 5:
        but5.config(image=img, bg='#D33333')
        but5["state"] = DISABLED
    if id == 6:
        but6.config(image=img, bg='#D33333')
        but6["state"] = DISABLED
    if id == 7:
        but7.config(image=img, bg='#AD1B1B')
        but7["state"] = DISABLED
    if id == 8:
        but8.config(image=img, bg='#AD1B1B')
        but8["state"] = DISABLED
    if id == 9:
        but9.config(image=img, bg='#AD1B1B')
        but9["state"] = DISABLED
def ButClick(id):
    global ActivePlayer
    global p1
    global p2
    global lab
    if ActivePlayer == 1:
        setLoyet(id, imgx)
        p1.append(id)
        lab = Label(window, image=img2, bg='#BBD7A3', height=50).grid(row=0, column=0,columnspan=3, sticky=N+S+W+E)
        ActivePlayer = 2
        print(p1)
    elif ActivePlayer == 2:
        setLoyet(id, imgo)
        p2.append(id)
        lab = Label(window, image=img1, bg='#D7A3A3', height=50).grid(row=0, column=0, columnspan=3,sticky=N + S + W + E)
        ActivePlayer = 1
        print(p2)
    CheckWiner()
def CheckWiner():
    Winer=-1
    if 1 in p1 and 2 in p1 and 3 in p1:
        Winer=1
    if 4 in p1 and 5 in p1 and 6 in p1:
        Winer=1
    if 7 in p1 and 8 in p1 and 9 in p1:
        Winer=1

    if 1 in p1 and 4 in p1 and 7 in p1:
        Winer=1
    if 2 in p1 and 5 in p1 and 8 in p1:
        Winer=1
    if 3 in p1 and 6 in p1 and 9 in p1:
        Winer=1

    if 1 in p1 and 5 in p1 and 9 in p1:
        Winer=1
    if 7 in p1 and 5 in p1 and 3 in p1:
        Winer=1



    if 1 in p2 and 2 in p2 and 3 in p2:
        Winer=2
    if 4 in p2 and 5 in p2 and 6 in p2:
        Winer=2
    if 7 in p2 and 8 in p2 and 9 in p2:
        Winer=2

    if 1 in p2 and 4 in p2 and 7 in p2:
        Winer=2
    if 2 in p2 and 5 in p2 and 8 in p2:
        Winer=2
    if 3 in p2 and 6 in p2 and 9 in p2:
        Winer=2

    if 1 in p2 and 5 in p2 and 9 in p2:
        Winer=2
    if 7 in p2 and 5 in p2 and 3 in p2:
        Winer=2
    if Winer == 1:
        messagebox.showinfo(title="Mebrooook", message="Player 1 win")
    if Winer == 2:
        messagebox.showinfo(title="Mebrooook", message="Player 2 win")
#
#
#
#
lab = Label(window, image=img1, bg='#D7A3A3', height=40).grid(row=0, column=0,columnspan=3, sticky=N+S+W+E)
#
but1 = Button(window, image=imgf, bg='#DF9C9C')
but1.grid(row=1, column=0, sticky=N+S+W+E)
but1.config(command=lambda: ButClick(1))
#
but2 = Button(window, image=imgf, bg='#DF9C9C')
but2.grid(row=1, column=1, sticky=N+S+W+E)
but2.config(command=lambda: ButClick(2))
#
but3 = Button(window, image=imgf, bg='#DF9C9C')
but3.grid(row=1, column=2, sticky=N+S+W+E)
but3.config(command=lambda: ButClick(3))
#
#
#
#
but4 = Button(window, image=imgf, bg='#C87676')
but4.grid(row=2, column=0, sticky=N+S+W+E)
but4.config(command=lambda: ButClick(4))
but5 = Button(window, image=imgf, bg='#C87676')
but5.grid(row=2, column=1, sticky=N+S+W+E)
but5.config(command=lambda: ButClick(5))
but6 = Button(window, image=imgf, bg='#C87676')
but6.grid(row=2, column=2, sticky=N+S+W+E)
but6.config(command=lambda: ButClick(6))
#
#
#
#
but7 = Button(window, image=imgf, bg='#B24A4A')
but7.grid(row=3, column=0, sticky=N+S+W+E)
but7.config(command=lambda: ButClick(7))
but8 = Button(window, image=imgf, bg='#B24A4A')
but8.grid(row=3, column=1, sticky=N+S+W+E)
but8.config(command=lambda: ButClick(8))
but9 = Button(window, image=imgf, bg='#B24A4A')
but9.grid(row=3, column=2, sticky=N+S+W+E)
but9.config(command=lambda: ButClick(9))
#
#
#
#
#
window.mainloop()
