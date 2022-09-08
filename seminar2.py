
# 1.На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной.


coins = {}
head_coins = 0
tails_coins = 0
import random
print('Minimum number of coins, enter the number of coins:')
number_of_coins = int(input())
for i in range(1, number_of_coins + 1):
    coins[i] = random.randint(0, 1)
    if coins[i] == 1:
        head_coins += 1
    else:
        tails_coins += 1
print(coins)
if head_coins < tails_coins:
    print('minimum number of coins - head coins = ', head_coins)
else:
    print('minimum number of coins - tails coins = ', tails_coins)

#-------------------------------------------------------------

# 2.Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

sum = 0
print('Sum of integers, enter the number (n):')
n = int(input())
for i in range(1, n + 1):
    sum = sum + i
print('Sum of integers = ', sum)

#--------------------------------------------------------------

# 3.Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

print('Smallest natural divisor, enter the number (n):')
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print('smallest natural divisor of numbers', n, ' = ', i)
        break

#---------------------------------------------------------

# 4.Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, 
# в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию 
# (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, 
# как у Пети, то программа должна расположить его после них.

petya_position = 1
number_of_students = 8
student_growth = 165, 163, 160, 160, 157, 157, 155, 154
print('Specify the height of the Petya (200 - 150):')
petya_growth = int(input())
for i in student_growth:
    if i < petya_growth:
        print('Petya position in the line = ', petya_position)
        break
    petya_position +=1

#--------------------------------------------------------

