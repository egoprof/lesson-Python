class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return (self.number_of_floors)
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    def __verify_type__(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError('Неправильный тип')
        return other if isinstance(other, int) else other.number_of_floors
    def __eq__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors == vv

    def __add__(self, value):
        if not isinstance(value, (int)):
            raise ArithmeticError('Неправильный тип')

        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.__add__(value)
        return self

    def __gt__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors > vv

    def __ge__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors >= vv

    def __lt__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors < vv

    def __le__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors <= vv

    def __ne__(self, other):
        vv = self.__verify_type__(other)
        return self.number_of_floors != vv

    def go_to(self,new_floor):
        t = new_floor > 0 and new_floor <= self.number_of_floors
        if t:
            for i in range (1, new_floor+1):
                print(i)
        else:
            print(f'Такого этажа не существует!')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print('----------------------------------------')
print('задание №2, module_5_2.py')
print('----------------------------------------')
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

print('----------------------------------------')
print('задание №3, module_5_3.py')
print('----------------------------------------')
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
