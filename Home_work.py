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


a = []
list = []

for element in input('Введите последовательность чисел: ').split(','):
    a.append(int(element))
    
for i in a:
    if i not in list:
        list.append(i)

print(a)
print(list)
