print('-'*5, 'Задача 1', '-'*5)
def text_screen():
    text = 'text.txt'
    try:
        with open(text, encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'Запрашиваемый файл не найден')

text_screen()

print('-'*5, 'Задача 2', '-'*5)

def two_num(num1, num2):
    try:
        while num1 == num2:
            print(f'Нулевой диапозон')
            break    
        assert type(num1) == int
        assert type(num2) == int
    except AssertionError:
        print(f'Неверный тип данных')
        # raise TypeError 
    else:
        for i in range(num1, num2):
            if i % 2 == 0:
                print(i)
        
tn = two_num(24, 24)
tn1 = two_num(24, [24])
tn2 = two_num(13, 21)

print('-'*5, 'Задача 3', '-'*5)

def square(len, sym, bool):
    try:
        assert type(len) == int
        while len <= 0:
            raise ValueError
    except AssertionError:
        # print(f'Неверный тип данных')
        raise TypeError
    except ValueError:
        print(f'Некорректного значения для переменной')

    line = len * sym
    if bool:
        for _ in range(len):
            print(line)
    else:
        print(line)
        for _ in range(len-2):
            print(sym + ' ' * (len-2) + sym)
        print(line)

square(6, '*', False)
print('-'*40)
square(5, '#', True)
print('-'*40)
square(-5, '#', True)
print('-'*40)
# square('a', '#', True)

print('-'*5, 'Задача 4', '-'*5)

def min_num(*args):
    try:
        while len(args) > 5:
            raise AttributeError
    except AttributeError:
        print(f'Функция не имеет данного атрибута')    
    else:
        print(f'Минимальное число: {min(args)}')

mn = min_num(2, -22, 6, 99, 0)
mn1 = min_num(2, -22, 6, 99, 0, 9)

print('-'*5, 'Задача 5', '-'*5)

def mult(num1, num2):
    try: 
        if num1 == num2:
            return f'Неверный диапозон'
        assert type(num1) == int
        assert type(num2) == int
        if num1 > num2:
            num1, num2 = num2, num1
        raise ValueError(num1 != num2)
    except AssertionError:
        raise TypeError
    except ValueError as err:
        print(f'Диапозон: {err}')
    x = 1
    for i in range(num1, num2 + 1):
        x *= i
    return x

mt = mult(2, 6)
print(mt)
mt1 = mult(5, 3)
print(mt1)
mt2 = mult(7, 7)
print(mt2)
# mt3 = mult(8, '2')
# print(mt3)


print('-'*5, 'Задача 6', '-'*5)

def len_num(num):
    try:
        assert type(num) == int
    except AssertionError:
        raise TypeError
    else:
        str_num = str(num)
        return f'Длина числа: {len(str_num)}'

# ln = len_num('35648')
# print(ln)
ln1 = len_num(35648)
print(ln1)

print('-'*5, 'Задача 7', '-'*5)

def Palindrome(num):
    try:
        assert type(num) == int
    except AssertionError:
        raise TypeError
     
    if str(num) == str(num)[::-1]:
        return f'Число палиндром'
    else:
        return f'Число не палиндром'
    
pl = Palindrome(121)
print(pl)
pl2 = Palindrome(123)
print(pl2)

print('-'*40)