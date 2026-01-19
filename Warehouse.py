from Inputs import input_product, input_price, input_quantity
from dataclasses import dataclass
from colorama import Fore, Back, Style
import logging


logger = logging.getLogger('store.warehouse')

@dataclass
class ProductInfo:
    # Цену и кол-во храним в датакласс объекте, чтобы проще было к ним обращаться
    price: float
    quantity: int

class Warehouse:
    def __init__(self):
        self._products = {'Пончик': ProductInfo(price=1.99, quantity=100),
                          'Сочник': ProductInfo(price=2.99, quantity=50),
                          'Сметанник': ProductInfo(price=2.50, quantity=42)}

    @property
    def products(self):
        if self._products:
            logger.info('Вывод списка товаров')
            print(f'\n{Back.YELLOW}{Fore.BLACK}Товары на складе:')

            for i, (product, info) in enumerate(self._products.items(), 1):
                print(f'{i}. Товар: {product}. '
                      f'Цена: {info.price} BYN. '
                      f'Количество: {info.quantity}.')

            print(Style.RESET_ALL)
        else:
            logger.warning('На складе не оказалось товаров')
            print(f'\n{Back.RED}{Fore.BLACK}Нет товаров на складе\n{Style.RESET_ALL}')

    def add_product(self):
        product = input_product()

        if product not in self._products:
            logger.info(f'Товар {product} добавлен на склад')
            self._products[product] = ProductInfo(price=input_price(), quantity=input_quantity())
            print(f'\n{Back.GREEN}{Fore.BLACK}Товар {product} добавлен на склад\n'
                  f'{Style.RESET_ALL}')
        else:
            logger.warning(f'Товар {product} уже есть на складе')
            print(f'\n{Back.RED}{Fore.BLACK}'
                  f'Товар {product} уже есть на складе\n'
                  f'Для изменения количества товара выберите пункт 3\n{Style.RESET_ALL}')

    def remove_product(self):
        product = input_product()

        if product in self._products:
            logger.info(f'Товар {product} удален')
            del self._products[product]
            print(f'\n{Back.GREEN}{Fore.BLACK}Товар {product} убран со склада\n'
                  f'{Style.RESET_ALL}')
        else:
            logger.warning(f'Товара {product} нет на складе')
            print(f'\n{Back.RED}{Fore.BLACK}Товар {product} отсутствует на складе\n'
                  f'{Style.RESET_ALL}')

    def change_quantity(self):
        product = input_product()

        if product in self._products:
            self._products[product].quantity = input_quantity()
            logger.info(f'Количество товара {product} изменено '
                        f'на {self._products[product].quantity} BYN')
            print(f'\n{Back.GREEN}{Fore.BLACK}'
                  f'Количество товара {product} изменено на {self._products[product].quantity}\n'
                  f'{Style.RESET_ALL}')
        else:
            logger.warning(f'Товар {product} отсутствует на складе')
            print(f'\n{Back.RED}{Fore.BLACK}Товар {product} отсутствует на складе\n'
                  f'{Style.RESET_ALL}')

    def change_price(self):
        product = input_product()

        if product in self._products:
            self._products[product].price = input_price()
            logger.info(f'Цена товара {product} изменена на {self._products[product].price}')
            print(f'\n{Back.GREEN}{Fore.BLACK}'
                  f'Цена товара {product} изменена на {self._products[product].price} BYN\n'
                  f'{Style.RESET_ALL}')
        else:
            logger.warning(f'Товар {product} отсутствует на складе')
            print(f'\n{Back.RED}{Fore.BLACK}Товар {product} отсутствует на складе\n'
                  f'{Style.RESET_ALL}')