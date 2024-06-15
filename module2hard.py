from random import randint
n = int(input("Введите число от 3 до 20: "))
result = ''
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            result += str(i) + str(j)

print("Для числа:", n, ", подойдет:", result)