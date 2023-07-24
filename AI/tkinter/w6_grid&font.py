from tkinter import *
from tkinter.font import *

def btnFunc1():
    label1.config(text="경제관의 학생 휴게실은 000호 입니다")
def btnFunc2():
    label1.config(text="호암관의 학생 휴게실은 000호 입니다")
def btnFunc3():
    label1.config(text="수선관의 학생 휴게실은 000호 입니다")
def btnFunc4():
    label1.config(text = "인문관의 학생 휴게실은 000호 입니다")

w6= Tk()
w6.title("학생 휴게실 정보")

#위젯 생성
f = Font(family = '함초롱바탕', size = 20)
btn1 = Button(w6, text = "경제관", command = btnFunc1)
btn2 = Button(w6, text = "호양관", command = btnFunc2)
btn3 = Button(w6, text = "수선관", command = btnFunc3)
btn4 = Button(w6, text = "인문관", command = btnFunc4)
label1 = Label(w6, text= "설명", font = f, fg='#ff0000', bg = '#ffff00')

#위젯배치 grid()
btn1.grid(row=0, column= 0)
btn2.grid(row = 0, column= 1)
btn3.grid(row= 1, column = 0)
btn4.grid(row=1, column = 1)
label1.place(x=0, y=150)

w6.geometry("300x100")
w6.mainloop()
