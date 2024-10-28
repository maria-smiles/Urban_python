calls = 0

# Функция count_calls подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls += 1

# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()

    return tuple((len(string), string.upper(), string.lower()))

# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string, list_to_search):
    count_calls()
    list_low = []

    for i in list_to_search:
        list_low.append(i.lower())

    if string.lower() in list_low:
        return True
    else:
        return False


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

