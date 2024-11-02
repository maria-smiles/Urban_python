
def calculate_structure_sum2(list_a, summa='None'):
    if summa == 'None':
        summa = 0
    else:
        summa = summa

    if isinstance(list_a, dict):
        dict_list = list(list_a.values())
        summa = calculate_structure_sum2(dict_list, summa=summa)
    for i in list_a:
        if isinstance(i, int):
#            print(f'суммирую число {i}')
            summa += i
        elif isinstance(i, str):
#           print(f'суммирую длину строки {i}')
            summa += len(i)
        else:
            summa = calculate_structure_sum2(i, summa=summa)
    return summa


data_structure = [
     [1, 2, 3],
     {'a': 4, 'b': 5},
     (6, {'cube': 7, 'drum': 8}),
     "Hello",
     ((), [{(2, 'Urban', ('Urban2', 35))}])]




result = calculate_structure_sum2(data_structure)

print(result)

