# Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int (input("Введите число N: "))
x = int (input ("Введите число X: "))
arr = []
from random import randint
for i in range(n):
    arr.append(randint(1, n))
print ("Задан массив: ")
print(arr)
y = abs(x - arr[0])
found = arr [0]
for i in range(1, len(arr)):
    if y > abs(arr[i] - x):
        y = abs(arr[i] - x)
        found = arr[i]

print(f'Ближайшее число будет {found}')