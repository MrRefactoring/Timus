"""
Задача  2095
Принцип работы алгоритма:

Вводим данные, после чего вызываем функцию func(x). x - аргумент, который содержит количество дней.
После чего выполняем цикл и возвращаем количество оставшихся дней.

"""

def func(x): # Объявляем функцию с именем func
    i = 2 # Присваиваем переменной i значение 2, т.к. программист начинает отчитываться каждые 2 дня
    while x >= i: # Пока количество дней больше чем количество отчетов
        x -= x // i # От количества дней отнимаем количество дней, которые были потрачены на отчеты
        i += 1 # В конце итераций добавляем +1 к проверочным дням
    return x # Возвращаем количество оставшихся дней


array = tuple(map(int, input().split())) # Переводим вводимые данные в кортеж (не в список, так как кортеж быстрее обрабатывается)
print(func(array[1]) - func(array[0] - 1)) # Выводим разность вызова функции func