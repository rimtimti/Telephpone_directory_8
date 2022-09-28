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



