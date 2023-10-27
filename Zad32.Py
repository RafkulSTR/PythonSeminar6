# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

number1 = int(input('Введите 1 число диапазона: '))
number2 = int(input('Введите 2 число диапазона: '))

list_1 = [random.randint(-100, 100) for i in range(20)]
print(list_1)
list_result = []
for i in range (len(list_1)):
    if number1 < list_1[i] < number2:
        list_result.append(i)
print(list_result)

