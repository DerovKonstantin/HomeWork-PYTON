# 1.Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

print('1.Enter the precision (the number of decimal places):')
decimal_places = int(input())
k = 0
pi = 0

for k in range(0, 10000):
    pi = pi +(1 /(16 **k)) *((4 /(8 *k +1)) -(2 /(8 *k +4)) -(1 /(8 *k +5)) -(1 / (8 *k +6 )))
text = str(pi)
print(text[0 :decimal_places +2])

#---------------------------------------------------------------

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('2.Enter natural number (N):')
n = int(input())
prime_number = 2
prime_factors = []
print('List of prime factors of ( N =', n, ') =>', end=' ')

while n/2 >= prime_number:
    if n % prime_number == 0:
        prime_factors.append(prime_number)
        n //= prime_number
    else:
        prime_number += 1
prime_factors.append(n)
print(prime_factors)

#---------------------------------------------------------------

# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

import random


list_elements = list()
print('3.Enter the size of the generated list:')
number_of_elements = int(input())
print('3.Enter the maximum random value:')
max_num_random = int(input())

for i in range(number_of_elements):
    list_elements.insert(0, random.randint(1, max_num_random))
print(list_elements)

i = 0
j = 0
for i in range(len(list_elements)):
    c = 0
    for j in range(i+1, len(list_elements)):
        if list_elements[j-c] == list_elements[i]:
            list_elements.pop(j-c)
            j=i+1
            c+=1
print('list of non-repeating elements =>', list_elements)
    
#for i in range(len(list_elements)): 
#    for j in range(i+1, len(list_elements)):
#        if list_elements[j] == list_elements[i]:
#            list_elements[j] = 0   #list_elements.pop(j)
#            print(list_elements, j)
#            c+=1
#            print(c)

#-------------------------------------------------------

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


list_of_coefficients = list()
list_natural_degree = [0, 0, 0, 0, 0]
k = list_natural_degree

print('4.Enter natural degree:')
natural_degree = int(input())
for i in range(0, natural_degree +1):
    list_natural_degree.pop(0)
    list_natural_degree.insert(len(list_natural_degree), i)

for i in range(5):
    list_of_coefficients.insert(0, random.randint(0, 100))

a = list_of_coefficients[0]
b = list_of_coefficients[1]
c = list_of_coefficients[2]
d = list_of_coefficients[3]
e = list_of_coefficients[4]

# взято с сайта - https://ru.stackoverflow.com/questions/1212304/python-%D0%9A%D0%B0%D0%BA-
# %D0%BD%D0%B0%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-
# %D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C-%D1%87%D0%B8%D1%81%D0%BB%D0%B0-
# %D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-
# %D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8E-print

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }

def degree(deg: int):
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees

print(k)
print(list_of_coefficients)
print('k=', natural_degree, '=>', a, 'x' ,end='')
print(degree(k[4]), '+' ,b, 'x', end='')
print(degree(k[3]), '+', c, 'x', end='')
print(degree(k[2]), '+', d, 'x', end='')
print(degree(k[1]), '+', e, 'x',end='')
print(degree(k[0]), '= 0')
    