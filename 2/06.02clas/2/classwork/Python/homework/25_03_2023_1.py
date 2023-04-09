#1 задание
print("1 zadan")
s = int(input("Введите начало диапазона "))  
e = int(input("Введите конец диапазона "))  
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
print( [ '{} - True'.format(i) for i in range(s,e)  if is_prime(i)]) 

#2 задание
print("2 zadan")
for i in range(1, 10+1): 
    print("\n")
    for j in range(1, 10+1):
        print(i, " * ", j, " = ", i*j) 
#3 задание
print("3 zadan")
s = int(input("Начало "))  
e = int(input("Конец "))  

for i in range(s, e+1): 
    print("\n")
    for j in range(s, e+1):
        print(i, " * ", j, " = ", i*j) 
