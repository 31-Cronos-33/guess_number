# Импорт функции получения случайных чисел из модуля random.
from random import randint as rnd


# Получаем случайное число в диапазоне от 1 до 100.
number = rnd(1, 100)
print('Угадайте число от 1 до 100')

while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Введите число: '))

    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
    
    # Если число больше загаданного...
    if guess > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')

    # Если число угадано...
    if guess == number:
        # ...Прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')