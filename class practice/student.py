class Student:

    def __init__(self, studentID, studentName, grade, address):
        # 객체. 메소드 
        # self는 Student 클래스 내의 속성 및 메소드를 지칭하는 방법임.
        self.studentID = studentID
        self.studentName = studentName 
        self.grade = grade
        self.address = address
    
    ## 메소드 
    def getStudentName(self) :
        return self.studentName
    def setStudentName(self, name) :
        self.studentName = name

    def sayHello(self) :
        return f"hi, my name is {self.name} and my studentID is {self.studentID}"

# 인스턴스 이름(변수명) = 클래스이름(클래스 멤버변수, ...)
# 인스턴스 = bill, elon, warren
bill = Student(5959, "Bill Gates", 1, "USA")
elon = Student(2222, "Elon Musk", 3, "Callifornia")
warren = Student(8282, "Warren Buffett", 2, "Korea")

print(bill.address)
print(elon.grade)
