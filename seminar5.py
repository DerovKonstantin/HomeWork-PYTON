# 1.Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from re import X


def Who_won (first, second):
    n = 0
    while n < 2021:
        if first > second:
            print('Первый игрок выбирает число от 1 до 28:')
            num_first = int(input())
            #num_first = 28
            if num_first < 1 or num_first > 28:
                print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 28:')
                second = 0
                first = 1
            else:
                n += num_first
                first = 0
                second = 1
                print('Колличество собранных конфет =>', n)
        else:
            print('Второй игрок выбирает число от 1 до 28:')
            num_second = int(input())
            #num_second = 28
            if num_second < 1 or num_second > 28:
                print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 28:')
                first = 0
                second = 1
            else:
                n += num_second
                second = 0
                first = 1
            print('Колличество собранных конфет =>', n)

    if first == 0:
        return print('!!!Выиграл первый игрок!!!')
    else :
        return print('!!!Выиграл второй игрок!!!')

def Who_won_bot (first, second, n):
    while n < 2021:
        if first > second:
            num_first = 28
            n += num_first
            first = 0
            second = 1
        else:
            num_second = 28
            n += num_second
            second = 0
            first = 1

    if first == 0:
        return 0
    else :
        return 1

def first_victory_conditions():
    first = 0
    second = 1
    win_list = list()
    for n in range(1, 29):
        if Who_won_bot (first, second, n) == 0:
            win_list.append(n)
    return win_list

def second_victory_conditions():
    first = 0
    second = 1
    win_list = list()
    for n in range(1, 29):
        if Who_won_bot (first, second, n) == 1:
            win_list.append(n)
    return win_list


def firstbot_always_wins(n_sum):
    first = 0
    second = 1
    win_list = list()
    for n in range(1, 29):
        if Who_won_bot (first, second, n_sum +n) == 0:
            win_list.append(n)
    return min(win_list), max(win_list)

def secondbot_always_wins(n_sum):
    second = 0
    first = 1
    win_list = list()
    for n in range(1, 29):
        if Who_won_bot (first, second, n_sum +n) == 1:#
            win_list.append(n)
    return min(win_list), max(win_list)

def Who_won_vs_bot (first, second):
    n = 0
    while n < 2021:
        if first > second:
            print('первый игрок выбирает число от 1 до 28:')
            num_first = int(input())
            if num_first < 1 or num_first > 28:
                print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 28:')
                second = 0
                first = 1
            else:
                n += num_first
                first = 0
                second = 1
                print('Колличество собранных конфет =>', n)
        else:
            print('второй игрок выбирает число от 1 до 28:')
            #print('ВЫБОРКА', min(secondbot_always_wins(n)), max(secondbot_always_wins(n)))
            num_second = random.randint(min(secondbot_always_wins(n)), max(secondbot_always_wins(n)))
            print(num_second)
            n += num_second
            second = 0
            first = 1
            print('Колличество собранных конфет =>', n)

    if first == 0:
        return print('выиграл первый игрок')
    else :
        return print('выиграл второй игрок')

def Who_won_bot_vs_bot (first, second):
    n = 0
    while n < 2021:
        if first > second:
            print('первый игрок выбирает число от 1 до 28:')
            print('ВЫБОРКА', min(firstbot_always_wins(n)), max(firstbot_always_wins(n)))##
            num_first = random.randint(min(firstbot_always_wins(n)), max(firstbot_always_wins(n)))
            print(num_first)
            n += num_first
            first = 0
            second = 1
            print('Колличество собранных конфет =>', n)
        else:
            print('второй игрок выбирает число от 1 до 28:')
            print('ВЫБОРКА', min(secondbot_always_wins(n)), max(secondbot_always_wins(n)))
            num_second = random.randint(min(secondbot_always_wins(n)), max(secondbot_always_wins(n)))
            print(num_second)
            n += num_second
            second = 0
            first = 1
            print('Колличество собранных конфет =>', n)

    if first == 0:
        return print('выиграл первый игрок')
    else :
        return print('выиграл второй игрок')

def Right_of_first_move ():
    print('ВНИМАНИЕ ЖЕРЕБЬЕВКА, угадайте число максимально близкое ЗАГАДАННОМУ ')
    print('Первый игрок выбирает число от 1 до 100')
    first = int(input())
    while first < 1 or first > 100:
        print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 100')
        first = int(input())
    print('Второй игрок выбирает число от 1 до 100')
    second = int(input())
    while second < 1 or second > 100 or second == first:
        print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 100')
        second = int(input())
    hidden_number = random.randint(1, 101)

    if abs(hidden_number - first) < abs(hidden_number - second):
        print('Загаданное число =>', hidden_number)
        print('!!!Право первого хода у первого игрока!!!')
        # first = 1, second = 0
        return 1, 0
    
    else:
        print('Загаданное число =>', hidden_number)
        print('!!!Право первого хода у второго игрока!!!')
        # first = 0, second = 1
        return 0, 1

print()
print('Игры с конфетами. Выберите возможные варианты соперничества:')
print('1.Противостояние двух игроков.')
print('2.Противостояние игрока и бота.')
print('3.Противостояние двух ботов " БОТЫ ЗАХОДЯТ В ТУПИК =) ".')

game = int(input())
while game < 1 or game > 3:
        print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 3')
        game = int(input())

print()
print('ВНИМАНИЕ!!! Вероятность выигрыша первого игрока повышается если на первом ходу выбирать цифры:')
print(first_victory_conditions())
print('Проигрышный вариант:')
print(second_victory_conditions())
print()

position = Right_of_first_move()
if game == 1:
    Who_won (position[0], position[1])
if game == 2:
    Who_won_vs_bot (position[0], position[1])
if game == 3:
    Who_won_bot_vs_bot(position[0], position[1])

#---------------------------------------------------

# 2.Создайте программу для игры в ""Крестики-нолики"".


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()

def input_matrix(matrix, z, text):
    x = 0
    y = 0
    s=''
    print(text, 'Укажите ряд (от 1 до 3)')
    y = int(input())
    while y < 1 or y > 3:
        print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 3')
        y = int(input())
    print(text, 'Укажите столбец (от 1 до 3)')
    x = int(input())
    while x < 1 or x > 3:
        print('НЕВЕРНОЕ ЧИСЛО!!! Число должно находится в диапазоне от 1 до 3')
        x = int(input())
    #matrix[y-1][x-1] = s
    if matrix[y-1][x-1] == 'O' or  matrix[y-1][x-1] == 'X':
        print('Данная позиция уже занята!')
        print_matrix(matrix)
        print('Введите данные заново !')
        input_matrix(matrix, z, text)
    else:
        matrix[y-1][x-1] = z
    return matrix

def hidden_symbol():
    hidden = random.randint(0, 1)
    if hidden == 0:
        return 'X'
    else:
        return 'O'

def player_symbol(hidden_symbol):
    symbol = str.upper(input())
    while symbol != 'X' and symbol != 'O':
        print('НЕВЕРНЫЙ СИМВОЛ!!! должен быть "X" или "O"')
        symbol = str.upper(input())
    if symbol == hidden_symbol:
        print('УГАДАЛ =>', hidden_symbol)
        return 1
    else:
        print('НЕ УГАДАЛ =>', hidden_symbol)
        return 0

def who_will_be_the_first():
    print()
    print('!!!КТО БУДЕТ ХОДИТЬ ПЕРВЫМ!!!')
    print('Первый игрок, угадайте "X" или "O"')
    first = player_symbol(hidden_symbol())
    print('Второй игрок, угадайте "X" или "O"')
    second = player_symbol(hidden_symbol())
    
    if first == second:
        print('НИЧЬЯ! НО, чтобы не затягивать пусть ходит первый игрок.')
        #print('НИЧЬЯ, попробуйте заново')
        return 0
        #who_will_be_the_first()
    if first > second:
        print('ПЕРВЫМ ХОДИТ "О" ПЕРВЫЙ ИГРОК')
        return 0
    if first < second:
        print('ПЕРВЫМ ХОДИТ "Х" ВТОРОЙ ИГРОК')
        return 1

def check_for_matches(count, matrix, symbol, text):
    if symbol == matrix[0][0] == matrix[1][1] == matrix[2][2]:
        print('Выиграл "', symbol,'"', text)
        return 10
    if symbol == matrix[0][1] == matrix[1][1] == matrix[2][1]:
        print('Выиграл "', symbol,'"', text)
        return 10
    if symbol == matrix[0][2] == matrix[1][1] == matrix[2][0]:
        print('Выиграл "', symbol,'"', text)
        return 10
    if symbol == matrix[1][0] == matrix[1][1] == matrix[1][2]:
        print('Выиграл "', symbol,'"', text)
        return 10
    else:
        return count +1

def who_will_win_at_tic_tac_toe():
    position = who_will_be_the_first()
    count = 0
    while count < 9:
        if count % 2 == position:
            input_matrix(matrix, 'O', 'ИГРОК 1')
            print_matrix(matrix)
            count = check_for_matches(count, matrix, 'O', ' ИГРОК 1')
            
        else:
            input_matrix(matrix, 'X', 'ИГРОК 2')
            print_matrix(matrix)
            count = check_for_matches(count, matrix,'X', ' ИГРОК 2')

print()
print('Крестики-нолики.')
matrix = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
print_matrix(matrix)
who_will_win_at_tic_tac_toe()
print()

#---------------------------------------------------------

# 3.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression_RLE(string):
    cout = 1
    result_str = ''
    i = 0
    while i < len(string) -1:
    
        if string[i] == string[i + 1]:
            cout += 1
            i+=1    
        else:
            result_str += str(cout) + string[i]
            cout = 1
            i+=1

    result_str += str(cout) + string[i]
    return result_str

#def decoding_RLE(string):
#    result_str = ''
#    count = ''
#    for i in string:
#        if i.isdigit():# isdigit - не хочет работать в методе
#            count += i
#        else:
#            result_str += i * int(count)
#            count = ''
#    return result_str

string = 'rrttyyyyyyyyyybbbbbbbbbbbiiiohhhhhhl'
#string = input()
print(string)
print(compression_RLE(string))
string = compression_RLE(string)
#print(decoding_RLE(string))

result_str = ''
count = ''
for i in string:
    if i.isdigit():
        count += i
    else:
        result_str += i * int(count)
        count = ''

print(result_str)

