# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.
# Пример: 
# 4, 4 >> 2, 2
# 5, 6 >> 2, 3

s = int (input ("Введите сумму загаданных чисел: "))
p = int (input ("Введите произведение загаданных чисел: "))

for i in range(s // 2 + 1):
    a = i
    b = s - i
    if a * b == p:
        print (f'Загаданные числа будут {a} и {b}')
        break
else:
    print ('Нет таких чисел, которые подходят по условию')