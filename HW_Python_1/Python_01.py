# 1) Создать переменную типа String
let_string = "Это строка"
# 2) Создать переменную типа Integer
let_integer = 2021
# 3) Создать переменную типа Float
let_float = 2021.2021
# 4) Создать переменную типа Bytes
let_bytes = bytes(702)
# 5) Создать переменную типа List
let_list_array = ['123', '456', 'asd', 'qwe', 23, True]
# 6) Создать переменную типа Tuple
let_tuple = (34, '23400', '1234', False)
# 7) Создать переменную типа Set
let_set = set({7, 07.02, 'evgenii'})
# 8) Создать переменную типа Frozen set
let_frozen_set = frozenset({7, 07.02, 'evgenii'})
# 9) Создать переменную типа Dict
let_dict = {'key1': 32,
            'key2': 23,
            'name': "evgenii",
            'age': 25}
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(let_string), let_string)
print(type(let_integer), let_integer)
print(type(let_float), let_float)
print(type(let_bytes), let_bytes)
print(type(let_list_array), let_list_array)
print(type(let_tuple), let_tuple)
print(type(let_set), let_set)
print(type(let_frozen_set), let_frozen_set)
print(type(let_dict), let_dict)
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name = 'evgenii'
name_2 = 'nata'
all_name = name + name_2
print(all_name)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую).
age = 25
print(name, age)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс).
print(name + str(age))