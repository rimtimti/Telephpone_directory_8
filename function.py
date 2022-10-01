import check as c
import json
import csv


def imp(list_of_data):
    """
    Импорт данных
    """
    # entry_f = input("Введите фамилию: ")
    # entry_n = input("Введите имя: ")
    # entry_tel = input("Введите номер телефона: ")
    # entry_about = input("Введите комментарий: ")
    with open('Telephone_base.txt', 'a', encoding="utf-8") as f:
        f.write('\n\r')
        f.write('\n'.join(list_of_data))


def read_base():
    '''
    Эспорт данных из файла txt в виде списка списков
    '''
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
    for i in range(int(len(lst)/6)+1):
        if text in lst[i]:
            temp = i % 6
            result = (lst[i-temp:i+5-temp])
            return text, result
    return text, "Данные отсутсвуют"

def choice():
    """
    Выбор операции
    """
    num = c.check_int_number("Импорт данных - 1\nЭкспорт данных - 2\n")
    return num

def read_csv():
    '''
    Чтение из файла csv, выводит массив строк
    '''
    with open('data.csv', encoding = 'utf-8') as file:
        file_reader = []
        for line in csv.reader(file, delimiter = '\t'):
            file_reader.append(' '.join(line))
        return file_reader

def write_csv(array):
    '''
    Запись в csv-файл массива строк
    '''
    with open('data.csv', mode ='a', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter='\t', lineterminator='\r')
        file_writer.writerow(array)

def write_json(array):
    '''
    Запись в json-файл массива строк
    '''
    with open('data.json', 'a') as file:
        json.dump(array, file, separators=(',', ':'), indent = 0)

def read_json():
    '''
    Чтение из файла json, выводит массив строк
    '''
    with open('data.json', encoding = 'utf-8') as file:
        text = file.read()
        
        # capitals_json = json.load(text)
        text = text.split('\n')
        return         text


print(read_json())
