import pytest
from Warehouse import Warehouse


def test_add_new_product(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value = 'Бублик')
    mocker.patch('Warehouse.input_quantity', return_value = 100)
    mocker.patch('Warehouse.input_price', return_value = 9.99)

    warehouse.add_product()
    assert 'Бублик' in warehouse._products
    assert warehouse._products['Бублик'].price == 9.99
    assert warehouse._products['Бублик'].quantity == 100

def test_add_existing_product(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value='Пончик')

    warehouse.add_product()
    assert sum(1 for product in warehouse._products if product == 'Пончик') == 1
    assert len(warehouse._products) == 3

def test_remove_existing_product(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value='Пончик')

    warehouse.remove_product()
    assert 'Пончик' not in warehouse._products

def test_remove_not_existing_product(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value='Корзиночка')

    warehouse.remove_product()
    assert len(warehouse._products) == 3

def test_change_quantity(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value = 'Пончик')
    mocker.patch('Warehouse.input_quantity', return_value = 200)

    warehouse.change_quantity()
    assert warehouse._products['Пончик'].quantity == 200

def test_change_price(mocker):
    warehouse = Warehouse()
    mocker.patch('Warehouse.print')
    mocker.patch('Warehouse.input_product', return_value='Пончик')
    mocker.patch('Warehouse.input_price', return_value=99.99)

    warehouse.change_price()
    assert warehouse._products['Пончик'].price == 99.99

