# Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'Vlad',
#     2: 'Vlad',
#     3: 'Oleg'
# }
# -> 2

my_dict = {
    "1": "Vlad", "2": "Vlad", "3": "Oleg"
    }
print(my_dict)

print(set(my_dict.values()))
