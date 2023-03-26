#1 задание
print("1 zadan")
print("Введите 2 числа")
q=int(input())
w=int(input())
s=0
s1=0
k=0
k1=0
for i in range(0,q+1):
    if(i%2==0 and i%9==0):
        s+=i
        k+=1
    else:
        s1+=i
        k1+=1
for j in range(0,w+1):
    if(j%2==0 and j%9==0):
        s+=j
        k+=1
    else:
        s1+=j
        k1+=1
print(s/k)
print(s1/k1)
#2 задание
print("2 zadan")
print("Введите длину линии и символ для заполнения")
e=int(input("Длина: "))
r=(input("Символ: "))
for i in range(0,e+1):
    print("\t\t\t",r)
#3 задание
print("3 zadan")
print("Введите числа")

y=int(input()) 
if(y==7):
    print("Good bue !")
elif(y<0):
    print("Number is negative")
elif(y==0):
    print("Number is equal to zero")
else:
    print("Number is positive")


#3 задание
print("4 zadan")
print("Введите числа")