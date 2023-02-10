# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# [4, 2, 2, 1, 5, 5]

# num = int(input('Василий хочет исправить плохую оценку на: '))
# list1 = [4, 2, 2, 1, 5,]
# for x in list1:
#     if num > min(list1):
#         if x == max(list1):
#             x = min(list1)
#     print(f'Вместо нормальных оценок, Василий получает {x}', end=' ')


def replace_marks(marks_list):
    for i in range(len(marks_list)):
        if (marks_list[i] == 5) or (marks_list[i] == 4):
            marks_list[i] = 2
    return marks_list

marks = [4, 2, 2, 1, 5, 5]
print(replace_marks(marks))
