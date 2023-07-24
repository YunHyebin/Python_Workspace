from tkinter import *
w = Tk()
# w.title("로그인")
# w.geometry("400x400")
# w.mainloop()
w.title("레이블 위젯 활용")
# PhotoImage함수를 통해 파일 경로로 사진 불러와 photo란 변수에 이미지 할당
photo = PhotoImage(file = "AI/tkinter/joongbu.png")
# AI\tkinter\joongbu.png
# 윈도우 창에 '중부대학교 사진' 글씨를 추가하고 파란색 글씨로 설정. 위젯만듬
label1 = Label(w, text = "중부대학교 사진", fg = "blue")
# 윈도우 창에 이미지 넣어 위젯 만듬
label2 = Label(w, image = photo)

# 위젯 화면에 배치
label1.pack()
label2.pack()
w.mainloop()