import log
# import json
import csv



def imp(list_of_data):
    """
    Импорт данных
    """
    log.logger(f"Пишем данные {list_of_data} в файл txt", "")

    with open('Telephone_base.txt', 'a', encoding="utf-8") as f:
        f.write('\n\r')
        f.write('\n'.join(list_of_data))


def read_base():
    '''
    Эспорт данных из файла txt в виде списка списков
    '''
    log.logger(f"Читаем данные из файла txt", "")
    with open('Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    result = []
    for i in range(int(len(lst)/6)+1):
        result.append(lst[i*6:i*6+5])
    return result


def exp(text):
    """
    Поиск и экспорт нужных данных
    """
    # text = input("Введите значение для поиска: ")
    with open('Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    for i in range(int(len(lst))+1):
        if text in lst[i]:
            temp = i % 6
            result = (lst[i-temp:i+5-temp])
            return text, result
    return text, "Данные отсутсвуют"

# def choice():
#     """
#     Выбор операции
#     """
#     num = c.check_int_number("Импорт данных - 1\nЭкспорт данных - 2\n")
#     return num


def read_csv():
    '''
    Чтение из файла csv, выводит массив строк
    '''
    log.logger(f"Читаем данные из файла csv", "")

    with open('data.csv', newline='\n', encoding = 'utf-8') as File:  
        reader = csv.reader(File, delimiter=',', lineterminator='\n')
        file_reader = []        
        for row in reader:
            file_reader.append(row)
    # print(file_reader)        
    return file_reader

def write_csv(array):
    '''
    Запись в csv-файл массива строк
    '''
    log.logger(f"Пишем данные {array} в файл csv", "")

    with open('data.csv', mode ='a', encoding='utf-8') as file:
     
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(array)

# def write_json(array):
#     '''
#     Запись в json-файл массива строк
#     '''
#     log.logger(f"Пишем данные {array} в файл txt", "")
    
#     with open('data.json', 'a') as file:
#         json.dump(array, file, separators=(',', ':'), indent = 0)

# def read_json():
#     '''
#     Чтение из файла json, выводит массив строк
#     '''
#     log.logger(f"Читаем данные из файла json", "")

#     with open('data.json', encoding = 'utf-8') as file:
#         text = file.read()
        
#         # capitals_json = json.load(text)
#         text = text.split('\n')
#         return         text
