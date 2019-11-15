alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmopqrstuvwxyzАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюяАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюя01234567890123456789"

encrypt = input("Речення: ")
key = int(input("ключ (1-25): "))
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Шифр: ", encrypted)
