from tkinter import *
from tkinter.font import *
w8 = Tk()
w8.title("랜선으로 떠나는 여행")

#창
topFrame = Frame(w8, width = 400, height = 50, bg = "green")
centerFrame = Frame(w8, width = 400, height = 50, bg = None)
bottomFrame = Frame(w8, width = 400, height = 250, bg= None)

#이미지 가져오기
photo1 = PhotoImage(file = "AI/tkinter/image/프랑스.PNG")
photo2 = PhotoImage(file = "AI/tkinter/image/이탈리아.PNG")
photo3 = PhotoImage(file = "AI/tkinter/image/스위스.PNG")
main = PhotoImage(file = "AI/tkinter/image/main.PNG")

#버튼 누르면 사진 띄우면서 글자 나타내기 함수
def btn1Func():
    lblImage.config(image= photo1)
    lblSpot.config(text= "프랑스 파리 - 에펠탑")

def btn2Func():
    lblImage.config(image= photo2)
    lblSpot.config(text = "이탈리아 로마 - 트레비분스")

def btn3Fucn():
    lblImage.config(image= photo3)
    lblSpot.config(text = "스위스 - 융프라우 산악열차")

curFont = Font(family= "나눔고딕", size = 20)


# 위젯생성
lblTitle = Label(topFrame, text= "랜선으로 떠나는 여행", width = 100, font = curFont, fg = "white", bg = "green")
btn1 = Button(centerFrame, text = '프랑스', font = curFont, command = btn1Func)
btn2 = Button(centerFrame, text = "이탈리아", font = curFont, command = btn2Func)
btn3 = Button(centerFrame, text= "스위스", font = curFont, command = btn3Fucn)
lblImage = Label(bottomFrame, image = main)
lblSpot = Label(bottomFrame, text = "런던 브릿지", font = curFont, fg = "red")

# 위젯 배치
lblTitle.pack(pady = 5)
btn1.pack(side = LEFT, padx = 10, pady =5)
btn2.pack(side = LEFT, padx = 10, pady = 5)
btn3.pack(side = LEFT, padx= 10, pady = 5)
lblImage.pack(pady = 5)
lblSpot.pack(pady = 5)

topFrame.pack(pady = 5)
centerFrame.pack(pady = 5)
bottomFrame.pack(pady = 5)

w8.geometry("400x550")
w8.resizable(False, False)
w8.mainloop()
