"""
программa Pomodoro.
На вход программа получает имя, фамилию, название задачи, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа
ведёт файл логов о всех запусках.
"""


import argparse
import datetime

from classes_time import Pomodoro

# переменные для вводимых данных

parser = argparse.ArgumentParser(description='Pomodoro')
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('name_of_task', type=str)
parser.add_argument('time_focus', nargs='?', type=float, default=25)
parser.add_argument('time_pause', nargs='?', type=float, default=5)
parser.add_argument('numb_of_cycles', nargs='?', type=int, default=4)

args = parser.parse_args()


# вывод заданных данных

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('name_of_task:', args.name_of_task)
print(f'time_focus: {args.time_focus} min')
print(f'time_pause: {args.time_pause} min')
print('numb_of_cycles:', args.numb_of_cycles)

# Выполнение программы с помощью импортированного класса Pomodoro

task = Pomodoro(args.time_focus, args.time_pause)

for i in range(args.numb_of_cycles):
    print(task.focus())
    print(task.pause())

print('End Pomodoro!')


# запись лога в файл

with open('Pomodoro_logs.txt', 'a') as f:
    f.write(f'{args.first_name} {args.last_name}, '
            f'task: {args.name_of_task}, '
            f'{datetime.datetime.now()} \n')


"""
Пример команды в консоли для выполнения:
при нахождении в директории с файлом программы

#: python pomodoro.py -fn Ivan -ln Ivanov math_task 15 5 5
(пользователь Иван Иванов мат. задача 
15 мин фокустровка, 5 мин перерыв, 5 циклов)

#: python pomodoro.py -fn Ivan -ln Ivanov math_task
(в данном случае прорамма будет работать с параметрами по умолчанию)
"""
