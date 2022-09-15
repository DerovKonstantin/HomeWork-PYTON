# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

arr = list()
import random
print('1.Enter the number of list items:')
number_of_list = int(input())
for i in range(number_of_list):
    arr.append(int(random.randint(1, 10)))
print(arr)

sum = 0
for i in range(1, len(arr), 2):
    sum += arr[i]
print(sum)

#----------------------------------------

# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = list()
import random
import math
print('2.Enter the number of list items:')
number_of_list = int(input())
for i in range(number_of_list):
    arr.append(int(random.randint(1, 10)))
print(arr)

for i in range(math.ceil(len(arr)/2)):
    arr[i] = arr[i] * arr[len(arr)-1]
    if i <= math.floor(len(arr)/2):
        arr.pop(len(arr) - 1)
print(arr) 

#----------------------------------------------

# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = list()
print('3.Enter the number of list items:')
number_of_list = int(input())
for i in range(number_of_list):
    arr.append(float(random.randint(100, 1000)/100))
print(arr)

max = arr[0] - int(arr[0])
min = arr[0] - int(arr[0])
for i in arr:
    i = i - int(i)
    if i > max:
        max = i
    if i < min:
        min = i
print('max', round(max, 3), '-', 'min', round(min, 3), '=>', round(max - min, 3))

#-------------------------------------------------------------------------------

# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

arr = list()
print('4.Enter decimal number:')
decimal_number = int(input())
print(decimal_number, end=' => ')
while decimal_number >= 1:
    if decimal_number % 2 == 0:
        arr.insert(0,0)
    else:
        arr.insert(0,1)
    decimal_number //= 2
for i in arr:
    print(i, end=' ')
print()
