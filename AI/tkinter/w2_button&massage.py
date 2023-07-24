from tkinter import *
from tkinter.messagebox import *

def Ok():
    print("확인 버튼을 누르셨습니다")
    showinfo("확인 버튼을 누르셨습니다")

def Cancel():
    print("취소 버튼을 누르셨습니다")
    showinfo("취소 버튼을 누르셨습니다")

w2 = Tk()
w2.title("버튼 위젯 활용")
btn1 = Button(w2, text = '확인', command= Ok)
btn2 = Button(w2, text = '취소', command= Cancel)
btn1.pack()
btn2.pack()
w2.mainloop()
