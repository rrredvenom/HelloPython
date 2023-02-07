# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# 1 1 2 3 5 8
# 5 -> 5
# 8 -> 6
# 7 -> -1

# a = int(input('Введите число: '))
# f = 2
# n1 = 1
# n2 = 0
# x = 0
# while a > x:
#    x = n1 + n2
#    n2 = n1
#    n1 = x
#    f += 1
# if a == x:
#    print(f'Является числом по счету {f - 1}')
# else:
#    print(-1)

n = int(input('n: '))
f_1 = 1
f_2 = 1
num_index = 2

while f_2 < n:
    num_index += 1
    f_1, f_2 = f_2, f_1 + f_2
    
if f_2 == n:
    print(num_index)
else:
    print(-1)
    
# print(num_index if f_2 == n else -1)

