def check_telephone_number(symbol: str) -> str:
    '''
    Поверка ввода номера телефона
    '''
    while True:
        try:
            number = input(symbol)
            if number  in '+123-4567890':
                return number
            else:
                print('Ошибка! Введены некорректные символы!')
        except ValueError:
            print('Ошибка! Введены некорректные символы!')


def check_int_number(number: str) -> int:
    '''
    Поверка на целое число
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print('Ошибка! Должно быть целое число!')
