import random
# n=10

# # while(n!=0):
# #     n-=1
# #     print(n)

# for i in range(0,10):
#     print(i)



# for i in range(10,0,-1):
#     print(i)


arr = [100]
m = 0
n = 100
k=0
u=0
print("Введите сравниваемое число ")
q=int(input())
print("Введите меняемое  число ")
w=int(input())
print("Введите число на которое надо поменять ")
e=int(input())
for i in range(0,100):
    arr.append(random.randint(-100,100))

for i in arr:
    print(i)
    m=max(m,i)
    n=min(n,i)
    if(i<0):
        k+=1
    if(i>q):
        u+=1
    for j in range(len(arr)):
        if(arr[i]==w):
            arr[i]=e
for i in arr:
    print(i)
print()
print()
print("max ",m)
print("min ",n)
print("Кол-во отриц. ",k)
print("больше n чисел ",u)
print(e)
print()
print()
for i in arr:
    print(i)
