from tkinter import *
w7 = Tk()
w7.title("랜선으로 떠나는 여행")

topFrame = Frame(w7, width = 400, height = 50, bg = "pink")
centerFrame = Frame(w7, width = 400, height = 50, bg= "green")
bottomFrame = Frame(w7, width = 400, height = 250, bg = "yellow")

topFrame.pack()
centerFrame.pack()
bottomFrame.pack()

w7.geometry('400x300')
w7.resizable(False, False)
w7.mainloop()
