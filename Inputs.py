from colorama import Fore, Back, Style # Модуль для разукрашивания консоли


def input_product():
    return input(f'{Style.BRIGHT}Введите название товара: ').strip().title()

def number_validation(msg, is_int=False):
    # Функция для валидации введенных чисел. Кол-во ожидаем инт, цену - float
    while True:
        data = input(Style.BRIGHT + msg).strip()
        try:
            value = int(data) if is_int else float(data)

            if value > 0:
                return value if is_int else round(value, 2)
            else:
                print(f'\n{Back.RED}{Fore.BLACK}Значение должно быть больше 0\n'
                      f'{Style.RESET_ALL}')

        except ValueError:
            print(f'\n{Back.RED}{Fore.BLACK}Некорректное значение\n'
                  f'{Style.RESET_ALL}')

def input_quantity():
    return number_validation('Введите количество: ', is_int=True)

def input_price():
    return number_validation('Введите цену: ', is_int=False)