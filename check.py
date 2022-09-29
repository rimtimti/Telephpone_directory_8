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

# check_choice_one_or_two
def check_int_number(digit: str) -> int:
    '''
    Проверка ввода 1 или 2
    '''
    while True:
        try:
            check_int_number = int(input(digit))
            if check_int_number == 1 or check_int_number == 2:
                return check_int_number
            else:
                print('Ошибка! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2')
        except ValueError:
            print('Ошибка! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2')
