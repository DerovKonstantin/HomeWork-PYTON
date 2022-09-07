# 6.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Input number of weekday:')
day = int(input())
if day < 1 or day > 7:
    print('Incorrect number of day')
elif day == 6 or day == 7:
    print(day, 'day of the week -> weekend ')
else:
    print(day, 'day of the week -> working ')

#----------------------------------------------------------------------

# 7.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print((not(x or y or z)) == (not(x) and not(y) and not(z)))

#----------------------------------------------------------------------

# 8.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('enter coordinate (x):')
x = int(input())
print('enter coordinate (y):')
y = int(input())
if x > 0 and y > 0:
    print('-> first quarter')
elif x > 0 and y < 0:
    print('-> second quarter')
elif x < 0 and y < 0:
    print('-> third quarter')
elif x < 0 and y > 0:
    print('-> fourth quarter')
else:
    print('-> point zero')

#------------------------------------------

# 9.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('enter quarter number(1-4):')
quarter = int(input())
if quarter < 1 or quarter > 4:
    print('Wrong number!')
elif quarter == 1:
    print('-> range of possible coordinates = х > 0, y > 0')
elif quarter == 2:
    print('-> range of possible coordinates = х > 0, y < 0')
elif quarter == 3:
    print('-> range of possible coordinates = х < 0, y < 0')
else:
    print('-> range of possible coordinates = х < 0, y > 0')

#-------------------------------------------

# 10.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
print('Enter the coordinate (x) of the first point:')
xa = int(input())
print('Enter the coordinate (y) of the first point:')
ya = int(input())
print('Enter the coordinate (x) of the second point:')
xb = int(input())
print('Enter the coordinate (y) of the second point:')
yb = int(input())
a_b = math.sqrt((xb-xa)**2+(yb-ya)**2)
print(round(a_b, 2))
