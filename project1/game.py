import numpy as np

def random_predict(number):# Функция подсчета кол-ва попыток    
    count = 0 # Переменная счетчик попыток    
    number = number # Переменная с рандомным числом в задонном диапазоне     
    min = 0 # Переменная с минимальным порогом    
    max = 100 # Переменная с максимальным порогом 
    
    while True: # Создаем бесконечный цикл пока верно
      predict = round((min+max)/2)
      count += 1      
      if number == predict: # Условие выхода из цикла
        break
      elif number > predict:
        min = predict
      elif number < predict:
        max = predict
    return count

# Функция подсчета среднего кол-ва попыток
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # Cписок для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел

    for number in random_array:# Перебираем 1000 попыток
        count_ls.append(random_predict(number)) # Заносим в список кол-во попыток

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
score_game(random_predict)