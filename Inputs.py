from colorama import Fore, Back, Style # Модуль для разукрашивания консоли
import logging

logger = logging.getLogger('logger.inputs')

def input_product():
    logger.info('Ввод названия товара')
    return input(f'{Style.BRIGHT}Введите название товара: ').strip().title()

def number_validation(msg, is_int=False):
    # Функция для валидации введенных чисел. Кол-во ожидаем инт, цену - float
    while True:
        data = input(Style.BRIGHT + msg).strip()
        try:
            value = int(data) if is_int else float(data)

            if value > 0:
                logger.info(f'Значение {value} принято')
                return value if is_int else round(value, 2)
            else:
                logger.error(f'Введено значение {value} <= 0')
                print(f'\n{Back.RED}{Fore.BLACK}Значение должно быть больше 0\n'
                      f'{Style.RESET_ALL}')

        except ValueError:
            logger.error(f'Введено некорректное значение {data}')
            print(f'\n{Back.RED}{Fore.BLACK}Некорректное значение\n'
                  f'{Style.RESET_ALL}')

def input_quantity():
    logger.info('Ввод количества')
    return number_validation('Введите количество: ', is_int=True)

def input_price():
    logger.info('Ввод цены')
    return number_validation('Введите цену: ', is_int=False)