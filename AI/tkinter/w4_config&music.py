# visual studio code로 실행중. 터미널 창에 pip install pygame 설치
# from pygame import mixer -> mixer.music.함수
from tkinter import *
from pygame.mixer import * #-> music.함수명

# 함수정의
def play():
    init() #init 함수는 초기화 함수
    music.load("AI/tkinter/farewell.mp3") #음악 파일 가져옴
    music.play() #음악재생

def stop():
    music.stop()

def view1():
    label2.config(image = photo1)

def view2():
    label2.config(image = photo2)


w4 = Tk()
w4.title("고양이의 가을")
photo1 = PhotoImage(file = "AI/tkinter/joongbu.png")
photo2 = PhotoImage(file = "AI/tkinter/joongbu2.png")

label1 = Label(w4, text = '어느덧 가을')
label2 = Label(w4, image = photo1)

btn1 = Button(w4, text = "처음", font = ("",20), command = view1)
btn2 = Button(w4, text= "사진", font = ("",20), command = view2)
btn3 = Button(w4, text= "재생", font = ("",20), command = play)
btn4 = Button(w4, text = "정지", font = ("",20), command = stop)

label1.pack()
label2.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
w4.mainloop()
