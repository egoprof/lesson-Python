import os.path
from pprint import pprint
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop:

    def __init__(self, file_name):
        self.__file_name = file_name
        self.get_products()

    def get_products(self):

        if os.path.isfile('Module_7_1.txt'):
            self.__file_name = "Module_7_1.txt"
            file = open(self.__file_name, 'r')
            inShop = file.read()
            file.close()
            return inShop
        else:
            self.__file_name = "Module_7_1.txt"
            file = open(self.__file_name, 'w')
            file.close()
            self.get_products()


    # Метод add(self, *products), который принимает неограниченное количество
    # объектов класса Product.
    # Добавляет в файл __file_name каждый продукт из products, если его ещё
    # нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку
    # 'Продукт <название> уже есть в магазине'
    def add(self, *products):
        for i in products:
            inShop = self.get_products()
            if i.name in inShop:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write( i.__str__())
                file.write('\n')
                file.close()


s1 = Shop("Module_7_1.txt")
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())