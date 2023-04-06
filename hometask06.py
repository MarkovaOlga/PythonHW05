# Дана строка(возможно,пустая),состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется
# количество повторений

def count_letters(input_list):
    result = []
    count = 1
    for i in range(len(input_list)):
        if i == len(input_list)-1:
            result.append(f"{input_list[i]}")
            if count > 1:
                result.append(f"{count}")
            break
        if input_list[i] == input_list[i+1]:
            count += 1
        if input_list[i] != input_list[i+1]:
            result.append(f"{input_list[i]}")
            if count > 1:
                result.append(f"{count}")
                count = 1
    return result

input_list = list(input("Введите в строку символы от A до Z: "))
if len(input_list) == 0:
    print("Вы не ввели символы")
else:
    print(*count_letters(input_list), sep="")