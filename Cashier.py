from Inputs import *
from Warehouse import Warehouse, ProductInfo
from colorama import Fore, Back, Style


class Cashier(Warehouse):
    def __init__(self):
        super().__init__()
        self._sold_products = {} # Отдельный дикт для хранения продаж за день
        self._total_sales = 0
        self._total_income = 0

    def __str__(self):
        if self._sold_products:
            header = f'\n{Back.YELLOW}{Fore.BLACK}Отчет за смену:\n'
            report_lines = []

            for i, (product, info) in enumerate(self._sold_products.items(), 1):
                report_lines.append(f'{i}. Товар: {product}. '
                      f'Всего продано: {info.quantity}, '
                      f'на сумму: {info.price} BYN.')

            footer = (f'\n\nВсего продаж: {self._total_sales}. '
                      f'Общая выручка: {self._total_income:.2f} BYN\n{Style.RESET_ALL}')
            return header + '\n'.join(report_lines) + footer
        else:
            return f'\n{Back.RED}{Fore.BLACK}Продажи отсутствуют\n{Style.RESET_ALL}'

    def sell_product(self):
        product = input_product()

        if product in self._products:
            quantity = input_quantity()
            total_price = self._products[product].price * quantity

            if quantity == self._products[product].quantity:
                print(f'\n{Back.GREEN}{Fore.BLACK}'
                      f'Товар {product} продан в количестве {quantity}\n'
                      f'Общая стоимость: {total_price} BYN\n'
                      f'ТОВАР ЗАКОНЧИЛСЯ НА СКЛАДЕ\n{Style.RESET_ALL}')
                del self._products[product] # Удаляем товар со склада, если он закончился
                self.sales_report(product, quantity, total_price) # При успешной продаже отдаем
                # данные в функцию, считающую продажи за день

            elif quantity < self._products[product].quantity:
                self._products[product].quantity -= quantity # Актуализируем кол-во на складе
                print(f'\n{Back.GREEN}{Fore.BLACK}'
                      f'Товар {product} продан в количестве {quantity}\n'
                      f'Общая стоимость: {total_price} BYN\n'
                      f'Остаток на складе: {self._products[product].quantity}\n'
                      f'{Style.RESET_ALL}')
                self.sales_report(product, quantity, total_price)

            else:
                print(f'\n{Back.RED}{Fore.BLACK}'
                      f'Количество {quantity} превышает остаток на складе! '
                      f'({self._products[product].quantity})\n{Style.RESET_ALL}')

        else:
            print(f'\n{Back.RED}{Fore.BLACK}'
                  f'Товар {product} отсутствует на складе\n{Style.RESET_ALL}')

    def sales_report(self, product, quantity, total_price):
        self._total_sales += quantity
        self._total_income += total_price

        if product not in self._sold_products:
            # Если первая продажа - добавляем продукт в отчет
            self._sold_products[product] = ProductInfo(price=total_price, quantity=quantity)
        else:
            # Если не первая - обновляем данные
            self._sold_products[product].price += total_price
            self._sold_products[product].quantity += quantity