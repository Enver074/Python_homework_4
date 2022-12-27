# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math

# d = float(input('Введите количество цифр после запятой: '))

# count = 0
  
# while d % 1 != 0:
#     d *= 10
#     count += 1
    
# print(round(math.pi, count))

# import math

# d = int(input('Введите количество цифр после запятой: '))

# print(round(math.pi, d))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Введите натеральное число: "))
# f = []
# d = 2
# m = n
# while d * d <= n:
#     if n % d == 0:
#         f.append(d)
#         n//=d
#     else:
#         d += 1
# f.append(n)
# print(f'{m} = {f}') 

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# a = []
# list = []

# for element in input('Введите последовательность чисел: ').split(','):
#     a.append(int(element))
    
# for i in a:
#     if i not in list:
#         list.append(i)

# print(a)
# print(list)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
 
print('Введите натуральную степень k:')
k = int(input())
 
def write_file(st):
    with open('Task4.txt', 'w') as data:
        data.write(st)
 
def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))    
    return list
    
def create_str(sp):
    list = sp[::-1]
    func = ''
    if len(list) < 1:
        func = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                func += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    func += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                func += f'{list[i]}x'
                if list[i + 1] != 0:
                    func += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                func += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                func += ' = 0'
    return func
 
koef = create_list(k)
write_file(create_str(koef))