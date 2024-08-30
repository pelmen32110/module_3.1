'''
Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True,
если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
'''
calls=0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple_=(len(string), string.upper(), string.lower())
    return tuple_

def is_contains(string,list_):
    count_calls()
    incl = string.lower() in [x.lower() for x in list_]
    return incl


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
