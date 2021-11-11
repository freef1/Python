# 1.Написать скрипт который в создаст список целых чисел.
int_list = list(range(1, 150))
print('int_list =', int_list)
# 2.Написать скрипт который в создаст список целых чётных чисел.
even_list = list(range(2, 200, 2))
print('even_list =', even_list)
# 3.Написать скрипт который в создаст список целых нечётных чисел.
odd_list = list(range(1, 201, 2))
print('odd_list =', odd_list)
# 4.Написать скрипт который из списка целых чисел выведет чётные числа.
for i in range(len(int_list)):
    if int_list[i] % 2 == 0:
        print('4.int_list[i] =', int_list[i])
# 5.Написать скрипт который из списка целых чисел выведет нечётные числа.
for i in range(len(int_list)):
    if int_list[i] % 2 != 0:
        print('5.int_list[i] =', int_list[i])
# 6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
for i in range(len(int_list)):
    if int_list[i] % 2 == 0:
        if int_list[i] % 5 == 0:
            print('6.int_list[i] =', int_list[i])
# 7.Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
count = []
for i in range(len(int_list)):
    if int_list[i] % 2 == 0:
        if int_list[i] % 5 == 0:
            list_5 = int_list[i]
            count.append(list_5)
print('count =', len(count))
# 8.Написать скрипт который в создаст список целых рандомных чисел.
import random

random_list = random.sample(range(1, 200), 99)
print('random_list =', random_list)


# 9.Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


print('split =', split(int_list, 5))
elem_5 = split(int_list, 5)


# 10.Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
def even_odd_list(arr):
    even = []
    odd = []
    for item in range(len(arr)):
        if arr[item] % 2 == 0 and arr[item] > 0:
            add_even = arr[item]
            even.append(add_even)
        elif arr[item] % 2 != 0:
            add_odd = arr[item]
            odd.append(add_odd)
    print('четный список =', even)
    print('нечетный список =', odd)


even_odd_list(int_list)
# 11.Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
# stars_5 = []
# for it in range(len(elem_5)):
#     stars_5 = stars_5 + elem_5[it]
# print(stars_5)
stars_5 = []
for it in range(40):
    stars = random.sample(range(1, 100), 5)
    stars_5.append(stars)
print(stars_5)
# 12.Написать скрипт который выведет список из сумм каждого внутреннего списка из 5_stars
summa_5 = []
for it in range(len(stars_5)):
    summa = sum(stars_5[it])
    summa_5.append(summa)
print(summa_5)
# 13.Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из
# 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится,
# то вместо него вернуть текст “No lists”
def spl(arr):
    sum_100 = []
    sum_99 = []
    for item in range(len(arr)):
        if sum(arr[item]) >= 100:
            add_sum_100 = arr[item]
            sum_100.append(add_sum_100)
        elif sum(arr[item]) < 100:
            add_sum_99 = arr[item]
            sum_99.append(add_sum_99)
    if sum_100 == []:
        print("No lists - sum >= 100")
    else:
        print('sum >= 100', sum_100)
    if sum_99 == []:
        print("No lists - sum < 100")
    else:
        print('sum < 100', sum_99)


spl(stars_5)
# 14.Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$,
# 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
def salary(age):
    if age >= 0 and 100 > age:
        if age >= 18 and 28 > age:
            print('За 5 лет вы сумеете отложить 10000$')
            print('За 8 лет вы сумеете отложить 20000$')
            print('За 10 лет вы сумеете отложить 30000$')
            print('За 12 лет вы сумеете отложить 50000$')
            print('За 15 лет вы сумеете отложить 100000$')
        elif age >= 28 and 42 > age:
            print('За 4 года вы сумеете отложить 10000$')
            print('За 6 лет вы сумеете отложить 20000$')
            print('За 8 лет вы сумеете отложить 30000$')
            print('За 9 лет вы сумеете отложить 50000$')
            print('За 12 лет вы сумеете отложить 100000$')
        elif age >= 42 and 63 > age:
            print('За 1 год вы сумеете отложить 10000$')
            print('За 1,5 года вы сумеете отложить 20000$')
            print('За 2 года вы сумеете отложить 30000$')
            print('За 3 лет вы сумеете отложить 50000$')
            print('За 5 лет вы сумеете отложить 100000$')
        elif age >= 63 and 100 > age:
            print('Пора отдохнуть от работы')
        elif age < 18:
            print('Рано думать о деньгах, нужно учиться')
    else:
        print('Введите ваш возраст от 0 до 100')


salary(25)


