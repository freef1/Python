import names
import randomtimestamp as rd
import random
import string
# 1.Написать скрипт который в создаст список целых чисел.
int_list = list(range(1, 150))
print('1 =', int_list)
# 2.Написать скрипт который в создаст список целых чётных чисел.
even_list = list(range(2, 200, 2))
print('2 =', even_list)
# 3.Написать скрипт который в создаст список целых нечётных чисел.
odd_list = list(range(1, 201, 2))
print('3 =', odd_list)
# 4.Написать скрипт который из списка целых чисел выведет чётные числа.
for i in int_list:
    if i % 2 == 0:
        print('4 =', i)
# 5.Написать скрипт который из списка целых чисел выведет нечётные числа.
for i in range(len(int_list)):
    if int_list[i] % 2 != 0:
        print('5 =', int_list[i])
# 6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
for i in range(len(int_list)):
    if int_list[i] % 2 == 0:
        if int_list[i] % 5 == 0:
            print('6 =', int_list[i])
# 7.Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
count = []
for i in int_list:
    if i % 2 == 0:
        if i % 5 == 0:
            list_5 = i
            count.append(list_5)
print('7 = count =', len(count))
# 8.Написать скрипт который в создаст список целых рандомных чисел.
random_list = random.sample(range(1, 200), 99)
print('8 = random_list =', random_list)
# 9.Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


print('9 = split =', split(int_list, 5))
elem_5 = split(int_list, 5)
# 10.Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.


def even_odd_list(arr):
    even = []
    odd = []
    for item in arr:
        if item % 2 == 0 and item > 0:
            add_even = item
            even.append(add_even)
        elif item % 2 != 0:
            add_odd = item
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
print('11 =', stars_5)
# 12.Написать скрипт который выведет список из сумм каждого внутреннего списка из 5_stars
summa_5 = []
for it in stars_5:
    summa = sum(it)
    summa_5.append(summa)
print('12 =', summa_5)
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
    if not sum_100:
        print("No lists - sum >= 100")
    else:
        print('sum >= 100', sum_100)
    if not sum_99:
        print("No lists - sum < 100")
    else:
        print('sum < 100', sum_99)


spl(stars_5)
# 14.Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$,
# 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.


def salary(age):
    if 0 <= age < 100:
        if 18 <= age < 28:
            print('За 5 лет вы сумеете отложить 10000$')
            print('За 8 лет вы сумеете отложить 20000$')
            print('За 10 лет вы сумеете отложить 30000$')
            print('За 12 лет вы сумеете отложить 50000$')
            print('За 15 лет вы сумеете отложить 100000$')
        elif 28 <= age < 42:
            print('За 4 года вы сумеете отложить 10000$')
            print('За 6 лет вы сумеете отложить 20000$')
            print('За 8 лет вы сумеете отложить 30000$')
            print('За 9 лет вы сумеете отложить 50000$')
            print('За 12 лет вы сумеете отложить 100000$')
        elif 42 <= age < 63:
            print('За 1 год вы сумеете отложить 10000$')
            print('За 1,5 года вы сумеете отложить 20000$')
            print('За 2 года вы сумеете отложить 30000$')
            print('За 3 лет вы сумеете отложить 50000$')
            print('За 5 лет вы сумеете отложить 100000$')
        elif 63 <= age < 100:
            print('Пора отдохнуть от работы')
        elif age < 18:
            print('Рано думать о деньгах, нужно учиться')
    else:
        print('Введите ваш возраст от 0 до 100')


salary(25)
# 15.Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль
# прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту
# развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of
# function body logic#
#
# 16.Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
user_name = []
for i in range(70):
    us_name = names.get_full_name()
    user_name.append(us_name)
print('16 =', user_name)
# 17.Написать скрипт который сгенерирует список имён файлов. К каждому имени файла надо прикрепить номер итерации
# цикла как порядковый номер.
h = 1
iter_names = []
for i in user_name:
    iter_names.append(str(h) + '.File.' + str(i) + '.txt')
    h += 1
print('17 =', iter_names)
# 18.Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это
# имя пользователя, а 1-й - элемент это дата регистрации.
ls_list = []
for i in user_name:
    us_name = i
    date_reg = rd.random_date()
    reg_name = [us_name] + [str(date_reg)]
    ls_list.append(reg_name)
print('18 =', ls_list)
# 19.Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
Employees = []


def random_password_1(n_symbol):
    return ''.join(random.choice(string.digits + string.ascii_letters) for x in range(n_symbol))


def random_email_1(n_symbol):
    return ''.join(random.choice(string.digits) for x in range(n_symbol))


random_login = []
for i in user_name:
    use_name = i.split(' ', 1)[1]
    login = use_name + random_password_1(2)
    random_login.append(login)
print(random_login)
random_password = []
for i in range(len(user_name)):
    random_password.append(random_password_1(12))
print(random_password)
random_email = []
for i in user_name:
    use_name = i.split(' ', 1)[0]
    email = use_name + random_email_1(2) + "@gmail.com"
    random_email.append(email)
print(random_email)
for i in range(len(user_name)):
    _0 = ls_list[i][0]
    _1 = random_login[i]
    _2 = random_password[i]
    _3 = random_email[i]
    _4 = ls_list[i][1]
    add = [_0] + [_1] + [_2] + [_3] + [_4]
    Employees.append(add)
print('19 =', Employees)
# 20.Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),
family = []
for i in Employees:
    log = i[1]
    use = i[0]
    bool = random.choice([True, False])
    add = [log] + [use] + [bool]
    family.append(add)
print('20 =', family)
# 21.Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
gender = []
for i in Employees:
    log = i[1]
    use = i[0]
    gend = random.choice([1, 0])
    add = [log] + [use] + [gend]
    gender.append(add)
print('21 =', gender)
# 22.Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
salary = []
for i in Employees:
    log = i[1]
    use = i[0]
    salar = str(random.randint(300, 5000)) + '$'
    add = [log] + [use] + [salar]
    salary.append(add)
print('22 =', salary)
# 23.Написать скрипт который создаст список имён работников из salary у которых ЗП от 1500$ до 3000$
s_1500_3000 = []
for i in salary:
    sal = (i[2])[:len(i[2]) - 1]
    if 1500 <= int(sal) <= 3000:
        s_1500_3000.append(i[1])
print('23 =', s_1500_3000)
# 24.Написать скрипт который создаст список имён мужчин из gender.
male = []
for i in gender:
    if i[2] == 1:
        male.append(i[1])
print('24 =', male)
# 25.Написать скрипт который создаст список имён женщин из gender.
female = []
for i in gender:
    if i[2] == 0:
        female.append(i[1])
print('25 =', female)
# 26.Написать скрипт который создаст список имён неженатых мужчин из family.
male_f = []
for i in range(len(family)):
    if family[i][2] == False and gender[i][2] == 1:
        male_f.append(family[i][1])
print('26 =', male_f)
# 27.Написать скрипт который создаст список имён незамужних женщин из family.
female_f = []
for i in range(len(family)):
    if family[i][2] == False and gender[i][2] == 0:
        female_f.append(family[i][1])
print('27 =', female_f)
# 28.Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте
# Employees, family, gender, salary. Реализуйте как скрипт, без функций
male_salary = []
for i in range(len(Employees)):
    sal = (salary[i][2])[:len(salary[i][2]) - 1]
    if int(sal) >= 1500 and gender[i][2] == 1 and family[i][2] == False:
        male_salary.append(Employees[i][0])
print('28 =', male_salary)
# 29.Реализуйте пункт 28 через через функции.


def employees (names, family, gender, salary):
    male_salary = []
    for i in range(len(names)):
        sal = (salary[i][2])[:len(salary[i][2]) - 1]
        if int(sal) >= 1500 and gender[i][2] == 1 and family[i][2] == False:
            male_salary.append(names[i][0])
    print('29 =', male_salary)


employees(Employees, family, gender, salary)
# 30.Поешьте и выспитесь)
# nnnn = []
# for i in range(40):
#     male = names.get_full_name(gender='male')
#     female = names.get_full_name(gender='female')
#     ran_name = random.choice([male, female])
#     if ran_name == male:
#         namem = ran_name + str(" 1")
#         print(namem)
#         nnnn.append(namem)
#     elif ran_name == female:
#         namef = ran_name + str(" 0")
#         nnnn.append(namef)
# print(nnnn)