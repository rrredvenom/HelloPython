# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# staert_list = [1, 2, 3, 4, 5]
# k = 3
# -> [3, 4, 5, 1, 2]

start_list = [1, 2, 3, 4, 5]
k = int(input('Enter K: '))
k = k % len(start_list)
result_list = [0, 0, 0, 0, 0]
i = 0
while i < len(start_list):
    if (i + k ) >= len(start_list) - 1:
        result_list[i + k - (len(start_list))] = start_list[i]
    else:
        result_list[i + k] = start_list[i]
    i += 1
print(result_list)

# k = 2
# start_list = [1, 2, 3, 4]
# new_list = []

# k = -(k%len(start_list))
# for i in start_list:
#     new_list.append(start_list[k])
#     k += 1
    
# print(new_list)

