# Скопировал входные данные из задания
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud = sorted(list(students))


lbook = dict(zip(stud,grades))
print('Проверка правильности создания словаря по алфавиту', lbook)
print('Всего студентов:', len(lbook))

#Создали список средних значений
ssum = {}
lsbook = {}
k = -1
for i in lbook.keys():
    k = k+1
    ssu = sum(lbook[i])/len(lbook[i])
    ssum[k] = ssu
    lsbook.update({stud[k]:ssum[k]})

print("У меня получилось:",lsbook)
print("  Должно быть так: {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}")
