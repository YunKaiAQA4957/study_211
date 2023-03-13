#Задача 1
tupl_1 = 5, 56, 9, 10, 10, 7, 5, 5, 58, 33
tupl_2 = 5, 15, 5 , 3, 45, 7, 9, 45, 5, 22
tupl_3 = 5, 44, 63, 3, 5, 7, 9, 9, 9, 63

print(*sorted(set(tupl_1).intersection(set(tupl_2).intersection(set(tupl_3)))))

print(*sorted(set(tupl_1) & set(tupl_2) & set(tupl_3)))


# #Задача 2
li = [tupl_1, tupl_2, tupl_3]
res = list(set([i for j in li for i in j]))
print(*sorted(res))


#Задача 3
for element in range(len(tupl_1)):
    if tupl_1[element] == tupl_2[element] == tupl_3[element]:
        print(f'Элемент {tupl_1[element]} на позиции {element}')


#Задача из журнала
def Convert(list):
    dict_0 = {}
    for key in list:
      dict_0[type(key)] = dict_0.get(type(key), 0) + 1
    doubles = {element: count for element, count in dict_0.items()}
    print(doubles)

Convert([6, '6', 5, '5', [6, '6'], ['5', 5], {6,5}, 5, 6, 23.3, 3.23])