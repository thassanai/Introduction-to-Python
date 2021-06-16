### Recursive Function ฟังก์ชันเรียกตัวเองใช้งาน
def a():
    print("A")
    b()

def b():
    print("B")

#a()

"""
หาจุดวนซ้ำ
หาจุดออกจาก function (return)
ต้องมี parameter

1-5 โดยไม่ใช้ คำสั่ง loop
"""

def addNumber(number):
    if number==5:
        return
    print(number+1) # 0
    number+=1 #1
    addNumber(number)    

addNumber(0)

###### ข้ามไป Assignment 02 factorial #####
def summation(number):
    if number==1:
        return number 
    else :
        return number+summation(number-1)


x=summation(10) # ? = 5+4+3+2+1
print(x)

"""
5
5 + summation(4)
5 + 4 + summation(3)
5 + 4 + 3 + summation(2)
5 + 4 + 3 + 2 + summation(2-1)
5 + 4 + 3 + 2 + 1
"""