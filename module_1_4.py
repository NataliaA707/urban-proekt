my_string = input('Введите Ваше ФИО: ')
print(my_string)
if my_string.count('а'):
    print('Количество символов: ', my_string.count('а'))
else:
    print('Символов не найдено')
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1:])
