from tkinter import *
from tkinter.messagebox import *
w3 = Tk()
w3.title("버튼과 엔트리 위젯 활용")
pw = Entry(w3)

def Ok():
    showinfo("이름", pw.get() + "님이 접속하셨습니다")

btn1 = Button(w3, text = "확인", command = Ok)
pw.pack()
btn1.pack()
w3.mainloop()
