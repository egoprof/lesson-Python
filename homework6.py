my_dict = {'Zaz': 1989, 'Volga': 2001, 'Lada': 1983}
print('Dict:',my_dict)
print('Existing value:', my_dict['Volga']) #Вывод значения года 'Volga'
print('Not existing value:', my_dict.get('Bmw')) #Нет в словаре 'Bmw'
my_dict.update({'Mercedes': 2004,
                'Toyota': 2017})
print('New Dict:',my_dict) #Добавлено ещё два элемента новых
print("Delete 'Zaz'")
print(my_dict.pop('Zaz')) #Выводит значение и удаляет из словаря
print(my_dict) #Показывает, что словарь пуст

my_set = {'1', 4, 5, 7, 4, 'G', 7, True, 9, '1', 1 ,9 , False, 4, 9, 'A', 5, True}
print('Вывод множества:', my_set)
my_set.update({'7', 3})
print('Вывод дополненного множества:', my_set) #До удаления
my_set.discard(3)
print('Вывлд с удалённым 4 элементом:', my_set) #После удаления 4 элемента (счёт с нуля)

