team1_num = int(input('Введите кол-во участников 1-ой команды: '))
team2_num = int(input('Введите кол-во участников 2-ой команды: '))
print('В команде Мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

score_1 = int(input('Введите кол-во решенных задач 1-ой команды: '))
score_2 = int(input('Введите количество задач решённых 2-ой командой: '))

print('Команда Мастера кода решила задач: {}'.format(score_1))
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print(f'Команды решили {score_1} и {score_2} задач')

team1_time = float(input('Время, за которое 1-ая команда решила задачи: '))
print('Команда Мастера кода решила задачи за {} c!'.format(team1_time))

team2_time = float(input('Время, за которое 2-ая команда решила задачи: '))
print('Волшебники данных решили задачи за {} c!'.format(team2_time))

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / 2
time_avg = round(time_avg, 2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')






