#1 задание
print("1 zadan")
print("Введите 2 числа")
q=int(input())
w=int(input())
print(q**w)
#2 задание
print("2 zadan")
for i in range(100,1000):
    b=i//100%10
    m=i//10%10
    n=i%10
    if(b==m or b==n or m==n or b==m==n):
        print(i)
#3 задание
print("3 zadan")
for j in range(100,10000):
    v=j//1000%10
    b=j//100%10
    m=j//10%10
    n=j%10
    if (v!=b and v!=m and v!=n and b!=m and b!=n and m!=n):
        print(v,b,m,n)
#4 задание
print("4 zadan")
e=int(input())
z=0
for h in e:
    if(h!=3 or h!=6):
        z+=h
        print(z)