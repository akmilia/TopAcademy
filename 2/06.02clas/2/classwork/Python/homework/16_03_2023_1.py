#1 задание
print("1 zadan")
print("Введите число в диапазоне от 1 до 100 ")
q=int(input())
if(q%3==0 and q%5==0):
    print("Fizz Buzz")
elif(q<1 or q>100):
    print("ОШИБКА, введите нужное число")
elif(q%3==0):
    print("Fizz")
elif(q%5==0):
    print("Buzz")
else:
    print(q)
#2 задание
print("2 zadan")
print("Введите число")
w=int(input())
print("В какую степень хотите возвести?")
print("0,1,2,3,4,5,6,7")
e=int(input())
if(e==0):
    print(e**0)
elif(e==1):
    print(e**1)
elif(e==2):
    print(e**2)
elif(e==3):
    print(e**3)
elif(e==4):
    print(e**4)
elif(e==5):
    print(e**5)
elif(e==6):
    print(e**6)
elif(e==7):
    print(e**7)
else:
    print("ОШИБКА, введите нужное число")
#3 задание
print("3 zadan")
print("Введите стоимость")
r=int(input())
print("Введите с какого на какой оператор вы хотите позвонить")
print("1)Билайн, 2)МТС, 3)Мегафон")
print("С какого звонить")
t=int(input())
print("на какой звонить")
y=int(input())
if(t==1 and y==1):
    print(r,"Между своими нет налогов")
elif(t==1 and y==2):
    print(r+7,"р")
elif(t==1 and y==3):
    print(r+12,"р")
elif(t==2 and y==1):
    print(r+8,"р")
elif(t==2 and y==2):
    print(r,"Между своими нет налогов")
elif(t==2 and y==3):
    print(r+7,"р")
elif(t==3 and y==1):
    print(r+5,"р")
elif(t==3 and y==2):
    print(r+6,"р")
elif(t==3 and y==3):
    print(r,"Между своими нет налогов")
else:
    print("ОШИБКА, введите нужные числа")
#4 задание
print("4 zadan")
print("Введите уровень продаж 3х менеджеров")
print("1")
z=int(input())
print("2")
x=int(input())
print("3")
c=int(input())
if(z<500):
    z+=200
    z=z+(z%100*3)
elif(z>500 and z<1000):
    z+=200
    z=z+(z%100*5)
elif(z>1000):
    z+=200
    z=z+(z%100*8)
else:
    print("Надбавки нема")

if(x<500):
    x+=200
    x=x+(x%100*3)
elif(x>500 and x<1000):
    x+=200
    x=x+(x%100*5)
elif(x>1000):
    x+=200
    x=x+(x%100*8)
else:
    print("Надбавки нема")

if(c<500):
    c+=200
    c=c+(c%100*3)
elif(c>500 and c<1000):
    c+=200
    c=c+(c%100*5)
elif(z>1000):
    c+=200
    c=c+(c%100*8)
else:
    print("Надбавки нема")
if(z>x and z>c):
    z+=200
    print("Лучший менеджер 1, его зарплата ", z)
if(x>z and x>c):
    x+=200
    print("Лучший менеджер 2, его зарплата ", x)
if(c>x and c>z):
    c+=200
    print("Лучший менеджер 3, его зарплата ", c)
