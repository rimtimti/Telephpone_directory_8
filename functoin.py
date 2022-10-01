import check as c

def imp():
    """
    Импорт данных
    """
    str1 = input("Введите фамилию: ")
    str2 = input("Введите имя: ")
    str3 = input("Введите номер телефона: ")
    str4 = input("Введите комментарий: ")
    with open('Telephpone_directory_8/Telephone_base.txt', 'a', encoding="utf-8") as f:
        f.write('\n' + str1 + '\n' + str2 + '\n' + str3 + '\n' + str4 + '\n')

def exp():
    """
    Поиск и экспорт нужных данных
    """
    text = input("Введите значение для поиска: ")
    with open('Telephpone_directory_8/Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    for i in range(len(lst)):
        if text in lst[i]:
            temp = i % 5
            result = (lst[i-temp:i+4-temp])
            return text, result
    return text, "Данные отсутсвуют"