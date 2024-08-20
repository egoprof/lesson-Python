from random import choice


print('-------------------------')
print(f'Первое задание:')
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

print('-------------------------')
print(f'Второе задание:')
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')
                print(line)
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print('-------------------------')
print(f'Третье задание:')
class MysticBall:
    def __init__(self, *words):
        self.word = words

    def __call__(self):
        words = choice(self.word)
        return words

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print('-------------------------')