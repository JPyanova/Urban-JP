def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['str', 2, True]
values_dict = {'a': 5, 'b': 6, 'c': 8}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['str_str', False]
print_params(*values_list_2, 42)
