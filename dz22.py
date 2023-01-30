try:
    with open("new.txt", 'w', encoding='cp1251') as q:
        q.write("Текст в файле")
        print("Файл создан, текст добавлен!")
        print('*'*40)
except Exception as e:
    print("Файл не создан")
    print(e)

file = open('new.txt')
print(file.read())

from functools import reduce 
print('example_1')
def formula():
    li = [43, 62, 71, 32, 44, 7, 1, 39]
    return reduce(lambda x, y: x + y, li)

print('Сумма списка:', formula())
sum_formula = formula()
print('Сохраненная в переменной', sum_formula)

def mul_s(a):
    return formula() + a

print(mul_s(0))
print(mul_s(10))
print(mul_s(100))
print(mul_s(-50))
print(mul_s(91))

print('*'*40)

print('example_2')

def mul_x(a):
        def formula():
            li = [43, 62, 71, 32, 44, 7, 1, 39]
            return reduce(lambda x, y: x + y, li) + a
        return formula

print(mul_x(5)())
print(mul_x(155)())
print(mul_x(305)())
print(mul_x(500)())

print('*'*40)

print('example_3')
def choosing_an_action(x, y):
    if x == '-':
        return sum_formula - y
    if x == '*':
        return sum_formula * y
    if x == '/':
        return sum_formula / y
    if x == '+':
        return sum_formula + y   
print(choosing_an_action('-', 300))
print(choosing_an_action('*', 10))
print(choosing_an_action('/', 10))
print(choosing_an_action('+',10))

input('Для выхода нажмите Enter')




print('*'*40)
input('Для выхода нажмите Enter')