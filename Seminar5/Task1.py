# Последовательностью Фибоначчи называется 
# последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

num = int(input('Введите число: '))
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list1 = []
for i in range (1, num + 1):
    list1.append(fib(i))
    print(list1)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
    

# n = int(input('--> '))
# result = fibonacci(n)
# print(result)

    