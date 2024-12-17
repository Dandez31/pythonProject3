def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


print_params()
print_params(5)
print_params(2, 'новая строка')
print_params(10, 'другая строка', False)
print_params (b=25)
print_params(c=[1, 2, 3])
print_params(a=4, c='новое значение')


def print_params(a, b, c):
    print(a, b, c)

values_list = [42, 'пример строки', False]
values_dict = dict(a=1, b='строка', c=True)
values_list_2 = [54.32, 'пример строки']
print_params(*values_list)
print_params(*values_list_2,42)
print_params(**values_dict)