import os, sys, io
from threading import Thread
from random import randint
from time import perf_counter, sleep
from distutils.dir_util import copy_tree


 
print('\n' + '+'*20 + ' Задание 1 ' + '+'*20 + '\n')


class my_Thread():
 
    def __init__(self):
        self.numbers = []
        self.average = 0
        self.summa = 0 
 
    def rnd(self):
        self.numbers = [randint(0, 100) for _ in range(20)]
    
    def summ(self):
        self.summa = sum(self.numbers)
 
    def avg(self):
        self.average = sum(self.numbers) / len(self.numbers)
 
m_thread = my_Thread()
 
start_time = perf_counter()

t1 = Thread(target=m_thread.rnd())
t2 = Thread(target=m_thread.summ())
t3 = Thread(target=m_thread.avg())
 
t1.start()
t1.join()

sleep(1)
 
t2.start()
t3.start()

end_time = perf_counter()

print(f'Полученный список: {m_thread.numbers}')
print(f'Сумма: {m_thread.summa}')
print(f'Среднее арифметическое: {m_thread.average}')
print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд')


print('\n' + '+'*20 + ' Задание 2 ' + '+'*20 + '\n')


dir_folder = input("Укажите путь и название файла: ")
folder_path = os.path.dirname(dir_folder)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def filling_file_num():
    filling_file_num.num = [randint(0, 100) for _ in range(20)]
    with open(dir_folder, 'w') as file:
        [file.write(str(i) + ', ') for i in filling_file_num.num]
    print(f'1. Файл создан в {dir_folder}')

def prime_num():
    in_file = os.path.join(sys.path[0], "C:/dz37/prime numbers.txt")
    with open(in_file, 'w') as file:
        [file.write(str(i) + ', ') for i in filling_file_num.num if i % 2 == 0]
    print(f'2. Простые числа найдены, сохранены в файл {in_file}')

def factorial():
    in_file = os.path.join(sys.path[0], "C:/dz37/factorial.txt")
    with open(in_file, 'w') as file:
        factorial = 1
        for i in filling_file_num.num:
            while i > 1:
                factorial *= i
                i -= 1
            file.write(str(factorial) + ',\n' + '\n')
    print(f'3. Факториал найден, сохранен в файле {in_file}')


start_time = perf_counter()

t1 = Thread(target=filling_file_num())
t2 = Thread(target=prime_num())
t3 = Thread(target=factorial())

t1.start()
t1.join()

t2.start()
t3.start()

sleep(1)

t2.join()
t3.join()

end_time = perf_counter()

print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд')


print('\n' + '+'*20 + ' Задание 3 ' + '+'*20 + '\n')


existing_directory = input('Укажите директорию из которой нужно скопировать файлы: ')
new_directory = input('Укажимте новую директорию куда нужно скопировать файлы: ')

def copy_file():
    copy_tree(existing_directory, new_directory)
    print('Копирование файлов завершено!')

start_time = perf_counter()

t1 = Thread(target=copy_file())

t1.start()
t1.join()

sleep(1)

end_time = perf_counter()

print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд')


print('\n' + '+'*20 + ' Задание 4 ' + '+'*20 + '\n')


existing_dir = input('Укажите директорию для поиска(напрмер: C:\dz37): ')
search_word = input('Введите слово для поиска: ')

li_file = [i for i in os.listdir(existing_dir) if i.endswith('.txt')]
print(f'Список файлов директории: {li_file}')


def srch_word():
    
    for files in li_file:
        with open(existing_dir + files, 'r', encoding='utf-8') as f:
            for line in f:
                if search_word in line:
                    srch_word.merge = os.path.join(sys.path[0], "C:/dz37/new/merge.txt")
                    if not os.path.exists('C:/dz37/new/'):
                        os.makedirs('C:/dz37/new/')
                    with open(srch_word.merge, 'a', encoding='utf-8') as outfile:
                        outfile.write(open(existing_dir +  files, 'r', encoding='utf-8').read())

def bad_words():
    bad_words.bad = os.path.join(sys.path[0], "C:/dz37/new/bad_words.txt")
    with open(bad_words.bad, 'w', encoding='utf-8') as bad_file:
        while True:
            bw = input(f'Введите плохие слова(* для выхода): ')
            if bw == '*':
                break
            bad_file.write(bw + '\n')

    with open(bad_words.bad, 'r', encoding='utf-8') as bad_file, open(srch_word.merge, 'r', encoding='utf-8') as outfile:
        bline = bad_file.read()
        bword = bline.split()
        line = outfile.read()
        l = line.split()
    with open(srch_word.merge, 'w', encoding='utf-8') as outfile:
        for r in l:
            if r not in bword:
                outfile.write(r + " ")
        

start_time = perf_counter()                   

t1 = Thread(target=srch_word())
t2 = Thread(target=bad_words())

t1.start()
t1.join()

t2.start()

sleep(1)

end_time = perf_counter()

print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд')