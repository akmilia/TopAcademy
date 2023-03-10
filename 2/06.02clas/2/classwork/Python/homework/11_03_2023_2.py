#1 задание
print("1 zadan")
print("Введите день недели")
print(1,2,3,4,5,6,7)
q=int(input())
if(q==1):
    print("Понедельник")
elif(q==2):
    print("Вторник")
elif(q==3):
    print("Среда")
elif(q==4):
    print("Четверг")
elif(q==5):
    print("Пятница")
elif(q==6):
    print("Суббота")
elif(q==7):
    print("Воскресенье")
else:
    print("ОШИБКА, введите нужную цифру")

#2 задание
print("2 zadan")
print("Введите номер месяца")
print(1,2,3,4,5,6,7,8,9,10,11,12)
w=int(input())
if(w==1):
    print("Январь")
elif(w==2):
    print("Февраль")
elif(w==3):
    print("Март")
elif(w==4):
    print("Апрель")
elif(w==5):
    print("Май")
elif(w==6):
    print("Июнь")
elif(w==7):
    print("Июль")
elif(w==8):
    print("Август")
elif(w==9):
    print("Сентябрь")
elif(w==10):
    print("Октябрь")
elif(w==11):
    print("Ноябрь")
elif(w==12):
    print("Декабрь")
else:
    print("ОШИБКА, введите нужную цифру")
#3 задание
print("3 zadan")
print("Введите цифру")
y=int(input())
if(y>0):
    print("Number is positive")
elif(y<0):
    print("Number is negative")
else:
    print("Number is equal to zero")

#4 задание
print("4 zadan")
print("Введите 2 числа")
a=int(input())
b=int(input())
if(a==b):
    print("Они равны")
elif(a>b):
    print(a,b)
else:
    print(b,a)