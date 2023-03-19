#Задача 1
def li_sort(list):
    arithmetic_mean = sum(list) / len(list)
    li_new = []
        
    if arithmetic_mean > 0:
        for i in range(0, len(list), 3):
            li_new.append(list[i:i + 3])
        print(sorted(li_new[0] + li_new[1]) + li_new[2][::-1])
    
    else:
        for i in range(0, len(list), 3):
            li_new.append(list[i:i + 3])
        print(sorted(li_new[0]) + (li_new[1] + li_new[2])[::-1])

li_sort([1, 55, 7, 6, 99, -129, 62, 97, 100, 22, 22])
li_sort([1, 55, 7, 6, 99, -129, 62, 97, -11100])


#Задача 2
rating_log = []
for i in range(1, 11):
    estimation = 0
    while estimation < 1 or estimation > 12:
        try:
            estimation = int(input(f'Введите {i} оценку: '))
        except:
            estimation = 0
    rating_log.append(estimation)
 
option = 0
while option == 0:
    print('\n1. Вывод списка оценок', '2. Пересдача экзамена', '3. Выходит ли стипендия',
          '4. Сортировка оченок по возрастанию', '5. Сортировка оченок по убыванию', '6. Выход', '\n', sep='\n')
    try:
        option = int(input())
        if option == 1:
            for i, val in enumerate(rating_log):
                print(i + 1, ' - ', val)
        elif option == 2:
            try:
                index = int(input('Введите номер экзамена: '))
                val = int(input('Введите оценку: '))
                if val > 0 and val < 13:
                    rating_log[index-1] = val
                    print('Оценка изменена')
            except:
                print('Ошибка!')
                option = 0
        elif option == 3:
            if sum(rating_log) / len(rating_log) >= 10.7:
                print('Стипендия выходит :)')
            else:
                print('Стипендия не выходит')
        elif option == 4:
            print(sorted(rating_log))
        elif option == 5:
            print(sorted(rating_log, reverse=True))
        if option != 6:
            option = 0
    except:
        option = 0

#Задача 3
def sort_li_bubble(list):
    counter = 0
    for _ in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]):
                list[j], list[j+1] = list[j+1], list[j]
                counter += 1
    print(f'Количество перестановок: {counter}')
    return list

sort_li_bubble = sort_li_bubble([55, 11, 2, -1, 10, 2, 102, 44, 66, 0])
print(sort_li_bubble)