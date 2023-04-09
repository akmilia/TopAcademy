#1 задание
print("1 zadan")
def palindrome(proving):
    s = proving.lower().replace(" ", "")
    return s == s[::-1]
    
phrase = input("Введите фразу: ")
if palindrome(phrase):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
#2 задание
print("2 zadan")
text = "Появился, значит, в Зоне Чёрный сталкер. К лагерю ночью повадился ходить и там сует руку в палатку и говорит: Водички попить! А если не дашь хлебнуть из фляжки или наружу полезешь — пришибет!  " 
spisok = input("List of words").split(",")  

for i in range(len(spisok)): 
    text.replace(spisok[i], spisok[i].lower()) 

print(text)
#3 задание
print("3 zadan") 
pred = "Появился, значит, в Зоне Чёрный сталкер. К лагерю ночью повадился ходить и там сует руку в палатку и говорит: Водички попить. А если не дашь хлебнуть из фляжки или наружу полезешь — пришибет." 
print("Кол-во предложений ", pred.find('.'))