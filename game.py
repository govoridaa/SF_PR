import numpy as np
# Переменная счетчик попыток
count = 0
# Переменная с рандомным числом в задонном диапазоне
number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
# Переменная с минимальным порогом 
min = 0
# Переменная с максимальным порогом 
max = 100
# Создаем бесконечный цикл пока верно
while True:
    predict = round((min+max)/2)
    #predict = int(input())
    count += 1
    # Условие выхода из цикла
    if number == predict:
        break
    elif number > predict:
        min = predict
        print(f"Угадываемое число больше {predict}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
    elif number < predict:
        max = predict
        print(f"Угадываемое число меньше {predict}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max+min)/2)}')


print(f"Вы угадали число {number} за {count} попыток.")