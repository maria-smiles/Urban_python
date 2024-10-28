# Задача "Распаковка":

def print_params(a = 8, b = '-----', c = False):
    print(f'a = {a}, b = {b}, c = {c}')

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['8-)', [6, 5, 4, 3], None]
values_dict = {'a': ('v', 5), 'b': 'cucumber', 'c': 0.0 }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)
