al = [
    "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", 
    "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", 
    "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", 
    "ю", "я"
]
k = int(input())
word = input()
enc_word = ""
for char in word:
    if char in al:
        current_index = al.index(char)
        new_index = (current_index + k) % len(al)
        enc_word += al[new_index]
    else:
        enc_word += char
print(f"Result: {enc_word}")
# класссссс
# я по клавишам толстыми пальцами не попадаю
# сикс севен 67 67 676 67 676 