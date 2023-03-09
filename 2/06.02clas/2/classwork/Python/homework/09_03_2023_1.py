#1 задание
print("1 zadan")
a=input()
b=input()
c=input()
print(a+b+c)
#2 задание
print("2 zadan")
print("Введите 4 значное число: ")
num = int(input("Введите целое: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)
#3 задание
print("3 zadan")
print("Введите количество метров: ")
q=int(input())
print("кол-во сантиметров",q*100)
print("кол-во дециметров",q*10)
print("кол-во миллиметров",q*1000)
print("кол-во миль", q/(1609))
print("5 zadan")
print("Введите основание и высоту треугольника: ")
s=int(input())
h=int(input())
print((s*h)/2)