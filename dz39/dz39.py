from threading import Thread

print('\n' + '+'*20 + ' 1 задание ' + '+'*20 + '\n')

def Coincidence1():
    with open('file.txt', 'r', encoding='utf-8') as f1, open('file1.txt', 'r', encoding='utf-8') as f2:
        
        for line1 in f1:
            for line2 in f2:
                if line1 != line2:
                    print(line1, line2)

def Coincidence2():
    with open('file.txt', 'r', encoding='utf-8') as f1, open('file1.txt', 'r', encoding='utf-8') as f2:
        
        for line1 in f1:
            for line2 in f2:
                if line1 == line2:
                    print(line1, line2)

t1 = Thread(target=Coincidence1)
t2 = Thread(target=Coincidence2)

t1.start()
t2.start()


print('\n' + '+'*20 + ' 2 задание ' + '+'*20 + '\n')

def number_sym():
    with open(r'file2.txt', 'r', encoding='utf-8') as file1, open('file out2.txt', 'w+', encoding='utf-8') as file2:
        characters = 0
        for _, line in enumerate(file1, 1):
            wl = line.split()
            characters += sum(len(i) for i in wl)
        file2.write(f'Количество символов:  {characters}\n')

def number_rows():
    with open(r'file2.txt', 'r', encoding='utf-8') as file1, open('file out2.txt', 'a', encoding='utf-8') as file2:
        lines = len(file1.readlines())
        file2.write(f'Количество строк:  {str(lines)}\n')

def vowel():
    with open(r'file2.txt', 'r', encoding='utf-8') as file1, open('file out2.txt', 'a', encoding='utf-8') as file2:
        l = file1.read()
        counter = 0
        for letter in l:      
            if letter in  ['а', 'А', 'у', 'У', 'о', 'О', 'е', 'Е', 'и', 'И', 'я', 'Я', 'ю', 'Ю', 'ё', 'Ё', 'э', 'Э', 'ы', 'Ы']:
                counter += 1              
        file2.write(f'Количество гласных:  {counter}\n')

def consonants():
    with open(r'file2.txt', 'r', encoding='utf-8') as file1, open('file out2.txt', 'a', encoding='utf-8') as file2:
        file1 = file1.read()
        counter = 0
        for letter in file1:      
            if letter in  ['б', 'Б', 'в', 'В', 'г', 'Г', 'д', 'Д', 'ж', 'Ж', 'з', 'З', 'й', 'Й', 'к', 'К', 'л', 'Л', 'м', 'М', 'н', 'Н',
                            'п', 'П', 'р', 'Р', 'с', 'С', 'т', 'Т', 'ф', 'Ф', 'х', 'Х', 'ц', 'Ц', 'ч', 'Ч', 'ш', 'Ш', 'щ', 'Щ']:
                counter += 1              
        file2.write(f'Количество согласных:  {counter}\n')

def digit():
    with open(r'file2.txt', 'r', encoding='utf-8') as file1, open('file out2.txt', 'a', encoding='utf-8') as file2:
        file1 = file1.read()
        counter = 0
        for num in file1:
            if num.isdigit():
                counter += 1
        file2.write(f'Количество цифр:  {counter}\n')

t3 = Thread(target=number_sym)
t4 = Thread(target=number_rows)
t5 = Thread(target=vowel)
t6 = Thread(target=consonants)
t7 = Thread(target=digit)

t3.start()
t4.start()
t5.start()
t6.start()
t7.start()


print('\n' + '+'*20 + ' 3 задание ' + '+'*20 + '\n')

def rem():
    with open(r'file3.txt', 'r', encoding='utf-8') as file3, open('file out3.txt', 'w', encoding='utf-8') as file3_1:
        line = file3.readline()
        line = line[:-1]
        file3_1.writelines(line)

t8 = Thread(target=rem)

t8.start()


print('\n' + '+'*20 + ' 4 задание ' + '+'*20 + '\n')

def st_len():
    with open(r'file4.txt', 'r', encoding='utf-8') as file4, open('file out4.txt', 'w+', encoding='utf-8') as file4_1:
        file4_1.write(max(file4, key = len))

t9 = Thread(target=st_len)

t9.start()


print('\n' + '+'*20 + ' 5 задание ' + '+'*20 + '\n')

def count_word():
    word = input('Введите слово: ')
    counter = 0
    with open(r'file5.txt', 'r', encoding='utf-8') as file5:
        for line in file5:
            words = line.split()
            for i in words:
                if i == word:
                    counter += 1
    print(f'Слово "{word}" встречается {counter} раз')

t10 = Thread(target=count_word)

t10.start()


print('\n' + '+'*20 + ' 6 задание ' + '+'*20 + '\n')

def repl_text():
    word = input('Введите искомое слово: ')
    word_repl = input('Введите слово для замены: ')
    with open(r'file6.txt', 'r', encoding='utf-8') as file6, open('file out6.txt', 'w', encoding='utf-8') as file6_1:
        wr = file6.read()
        wr = wr.replace(word, word_repl)
        file6_1.write(wr)

t11 = Thread(target=repl_text)

t11.start()