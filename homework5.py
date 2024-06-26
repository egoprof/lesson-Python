immutable_var = 5, 'Vasya', 7, True, 'School'
print(immutable_var)
print("Доказательство, что ячейка immutable_var является типом 'tuple':", type(immutable_var))

#Попытка изменить второй элемент кортежа на другое содержание
#immutable_var[1] = 'Petya'

# !! Внимание !!
#Закомментировал, так как даёт ошибку при изменении содержинии. В ранном типе 'tuple' нельзя
#выполнять данную операцию - данный тип для этого специально и создан - не изменять содержимое.
#Удобно, например, четкие имена элементов формы: 'мужчина', 'женщина'. При этом нет смысла менять
#содержимое, в течении работы программы и чтоб не сделать ошибку, такой тип 'tuple' очень удобен.
# + данный тип занимает меньше памяти.

mutable_list = [5, "Vasya", 7, True, "School"]
print("Новая ячейка mutable_list:", mutable_list)
print("Доказательство, что ячейка immutable_var является типом 'list':", type(mutable_list))
mutable_list[1] = 'Petya'
print("Показываю, что данный тип 'list' изменяет содержимое второго элемента:", mutable_list)