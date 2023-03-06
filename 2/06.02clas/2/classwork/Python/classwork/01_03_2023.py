# str_Hello = "Hello"

# test_mess = "Hello, my name is Chakki!\n Nice to meet you my favorite friend!\n"

# print(str_Hello.count(""))
# print(str_Hello)
# print(test_mess.count("\n"))
# print(test_mess.capitalize())
# print(test_mess.upper())
print("1)Hi! 2)My 3)name 4)Egorka")
qwerty = ("1)Hi! 2)My 3)name 4)Egorka")
print( qwerty[3:])
n=int(input())
print(qwerty[n:])
x=qwerty.replace(' ','\t')
print (x)
t=qwerty.split()
print("ВВедите  номер называемого слова")
m=int (input())
print("ВВедите  заменяемое слово называемого слова")
q= (input())
t[m]=q
print(" ".join(t))