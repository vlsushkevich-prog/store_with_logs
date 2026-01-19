from colorama import Fore, Back, Style
from Cashier import Cashier
from Menu import *
import logging


logger = logging.getLogger('store')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs.txt', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

cashier = Cashier()
state = 'main'
logger.info('Запуск магазина')

while True:
    if state == 'main':
        decision = main_menu()
        match decision:
            case '1':
                logger.info('Открыто меню кассы')
                state = 'cashier'
            case '2':
                logger.info('Открыто меню склада')
                state = 'warehouse'
            case '3':
                logger.info('Выход из программы')
                break
            case _:
                logger.error('Попытка выбора несуществующего пункта меню')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'cashier':
        decision = cashier_menu()
        match decision:
            case '1':
                logger.info('Старт продажи товара')
                cashier.sell_product()
            case '2':
                logger.info('Запрос отчета за смену')
                print(cashier)
            case '3':
                logger.info('Возврат в главное меню')
                state = 'main'
            case _:
                logger.error('Попытка выбора несуществующего пункта меню')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'warehouse':
        decision = warehouse_menu()
        match decision:
            case '1':
                logger.info('Запрос на добавление товара')
                cashier.add_product()
            case '2':
                logger.info('Запрос на удаление товара')
                cashier.remove_product()
            case '3':
                logger.info('Запрос на изменение количества')
                cashier.change_quantity()
            case '4':
                logger.info('Запрос на изменение цены')
                cashier.change_price()
            case '5':
                logger.info('Запрос списка товаров')
                cashier.products
            case '6':
                logger.info('Возврат в главное меню')
                state = 'main'
            case _:
                logger.error('Попытка выбора несуществующего пункта меню')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')