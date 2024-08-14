team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result

#team1_num = 5
print('В команде Мастера кода участников: %s !' % team1_num)
#team2_num = 6
print('В команде Мастера кода участников: %(tn1)s и %(tn2)s !' % {'tn1': team1_num, 'tn2': team2_num})
#score_2 = 42
print('Команда Волшебники данных решила задач: {score2} !'.format(score2 = score_2))
#team1_time = 18015.2
print('Команда Волшебники данных решила задач: {t1time} с !'.format(t1time = team1_time))
#score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
#challenge_result = 'победа команды Мастера кода'
print(f'Результат битвы: {challenge_result}!')
#tasks_total = 82
#time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')