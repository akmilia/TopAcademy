# def main():
#     n= -8
#     print_all_negagiv(n,55)

# def print_all_negagiv(n,size):
#     for i in range(n,size):
#         if i < 0 :
#             print (i)
#     test = 505


# print(test)


arr = [1,2,3,4]

for i in arr :
    print (end="i")


print ()
print ()
print ()
while True:
    a = int(input())
    b = int(input())
    print("+,-,*,/,%")
    c = input()
    if(c == "+"):
       print(a+b)
    elif(c == "-"):
        print(a-b)
    elif(c == "/"):
        print(a/b)
    elif(c == "%"):
        print(a%b)
    elif(c=="*"):
        print(a*b)
    else:
        break
