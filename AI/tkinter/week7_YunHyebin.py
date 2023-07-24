from tkinter import *
from pygame.mixer import *
from tkinter.font import *
from tkinter.messagebox import *


w = Tk()
w.title("노래 감상")
w.geometry("800x400+225+25")
w.resizable(True, True)


# 음악 목록 함수
def menu():
    menu = Tk()
    menu.title("음악 목록")
    menu.geometry("400x400")
    menu.resizable(True, True)
    btn_mommyson = Button(menu, text = "마미손-사랑은", command = mommyson)
    btn_mommyson.pack()
    
def mommyson():
    mommyson = Tk()
    mommyson.title("마미손 - 사랑은")
    
    btn_play = Button(mommyson, text= "재생", command = mommyson_play)
    btn_stop = Button(mommyson, text= "중지", command = stop)
    btn_play.pack()
    btn_stop.pack()

def stop():
    music.pause()

# 노래 재생 함수
def mommyson_play():
    init()
    music.load("AI/tkinter/farewell.mp3")
    music.play()

#첫 화면?
photo1 = PhotoImage(file = "AI/tkinter/음악감상.png")
font1 = Font(family = "고딕", size = 20, weight= BOLD)
label1 = Label(w, text= "음악 감상 페이지에 오신 것을 환영합니다", font = font1, bg = "#CCCCFF")
label2 = Label(w, image= photo1)
btn_menu = Button(w, text = "음악 목록", font = "고딕", command = menu)



label1.pack()
label2.pack()
btn_menu.pack()

w.mainloop()
