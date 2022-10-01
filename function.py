import check as c

def imp(list_of_data):
    """
    Импорт данных
    """
    # entry_f = input("Введите фамилию: ")
    # entry_n = input("Введите имя: ")
    # entry_tel = input("Введите номер телефона: ")
    # entry_about = input("Введите комментарий: ")
    with open('Telephpone_directory_8/Telephone_base.txt', 'a', encoding="utf-8") as f:
        f.write('\n\r')
        f.write('\n'.join(list_of_data))
                
def exp(text):
    """
    Поиск и экспорт нужных данных
    """
    # text = input("Введите значение для поиска: ")
    with open('Telephpone_directory_8/Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    for i in range(len(lst)):
        if text in lst[i]:
            temp = i % 6
            result = (lst[i-temp:i+5-temp])
            print (text, result)
            return text, result
    return text, "Данные отсутсвуют"

def choice():
    """
    Выбор операции
    """
    num = c.check_int_number("Импорт данных - 1\nЭкспорт данных - 2\n")
    return num

def read_base():
    '''
    Экспорт данных из файла в виде списка списков
    '''
    with open('Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    result = []
    for i in range(int(len(lst)/6)+1):
        result.append(lst[i*6:i*6+5])
    return result