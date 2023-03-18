#1 задание
print("1 zadan")
print("Введите 2 числа")
q=int(input())
w=int(input())
if(q>w):
    while(q>w):
        if(w%7==0):
            print(w)
        w+=1
elif(w>q):
    while(w>q):
        if(q%7==0):
            print(q)
        q+=1
else:
    print("Эти числа одинаковые")
#2 задание
print("2 zadan")
print("Введите 2 числа")
print("начало диапазона")
e=int(input())
print("конец диапазона")
r=int(input())
print(" ")
k=0
for i in range(e,r+1):
    print(i)
print(" ")
for i in range(r-1,e,-1):
    print(i)
print(" ")
for i in range(e,r+1):
    if(i%7==0):
        print(i)
print(" ")
for i in range(e,r+1):
    if(i%5==0):
        k+=1
print(k)
#3 задание
print("3 zadan")
print("начало диапазона")
a=int(input())
print("конец диапазона")
b=int(input())
for j in range(a,b+1):
    if(j%3==0 and j%5==0):
        print("Fizz buzz")
    elif(j%3==0):
        print("Fizz")
    elif(j%5==0):
        print("Buzz")
    else:
        print(j)