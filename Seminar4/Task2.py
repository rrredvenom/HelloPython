#  Пользователь вводит текст(строка). Словом считается
# последовательность непробельных 
# символов идущих подряд, слова разделены 
# одним или большим числом пробелов.Определите, сколько различных 
# слов содержится в этом тексте.
# 'qwrqw  qwr g,l;c wet 234      3dgs'
# -> 6

text = input('Введите текст: ')
list_text = text.split()
print(len(list_text))
