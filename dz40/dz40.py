import random
from linked_list import linked_list

print('\n' + '+'*20 + ' 1 задание ' + '+'*20 + '\n')

def Calculation():
    cal = input('Введите выражение: ')
    if '+' in cal:
        x, y = cal.split('+')
        print(f'Результат: {int(x) + int(y)}')
    elif '-' in cal:
        x, y = cal.split('-')
        print(f'Результат: {int(x) - int(y)}')
    elif '*' in cal:
        x, y = cal.split('*')
        print(f'Результат: {int(x) * int(y)}')
    elif '/' in cal:
        x, y = cal.split('/')
        print(f'Результат: {int(x) / int(y)}')

Calculation()

print('\n' + '+'*20 + ' 2 задание ' + '+'*20 + '\n')

res = [random.randrange(-2000, 5000) for i in range(10)]
li = linked_list()
print(f'Рандомный список: {res}')

def max_num():
    li.append(max(res))
    # li.display()
    return li

def min_num():
    li.append(min(res))
    # li.display()
    return li

def positive_num():
    li.append(sum(i > 0 for i in res))
    # li.display()
    return li

def negative_num():
    li.append(sum(i < 0 for i in res))
    # li.display()
    return li

def zero():
    li.append(sum(i == 0 for i in res))
    li.display()
    return li

max_num()
min_num()
positive_num()
negative_num()
zero()