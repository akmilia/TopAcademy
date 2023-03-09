#1 задание
print("1 zadan")
print("Введите 3 числа")
a=int(input())
b=int(input())
c=int(input())
print("Умножить:1\t Сумма:2\n")
q=int(input())
if(q==1):
    print(a*b*c)
elif(q==2):
    print(a+b+c)
else:
    print("ОШИБКА, введите нужную цифру")
#2 задание
print("2 zadan")
print("Введите 3 числа")
a_1=int(input())
b_1=int(input())
c_1=int(input())
print("мин:1\t макс:2\t сред:3\n")
q=int(input())
if(q==1):
    y=min(a_1,b_1,c_1)
    print(y)
elif(q==2):
    y=max(a_1,b_1,c_1)
    print(y)
elif(q==3):
    y=(a_1+b_1+c_1)/3
    print(y)
else:
    print("ОШИБКА, введите нужную цифру")
#3 задание
print("3 zadan")
print("Введите количество метров: ")
p=int(input())
print("мили:1\t дюймы:2\t ярды:3\n")
w=int(input())
if(w==1):
    z=p/1609
    print(z)
elif(w==2):
    z=p*39.37
    print(z)
elif(w==3):
    z=p*1.09
    print(z)
else:
    print("ОШИБКА, введите нужную цифру")