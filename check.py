def check_telephone_number(symbol: str) -> str:
    '''
    Проверка ввода номера телефона
    '''
    while True:
        try:
            number = input(symbol)
            if number  in '1234567890':
                return number
            else:
                print('Ошибка! Введены некорректные символы!')
        except ValueError:
            print('Ошибка! Введены некорректные символы!')

