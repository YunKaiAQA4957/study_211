import random as rnd

def random_arr(n):
    return [rnd.randint(0, 10) for _ in range(n)]

li_1 = random_arr(5)
li_2 = random_arr(5)

print(f'1-й список случайных чисел {li_1}')
print(f'2-й список случайных чисел {li_2}')

print('-'*40)

print(f'Список, содержащий элементы обоих списков: {[i for i in li_1 + li_2]}')
print(f'Список, содержащий элементы обоих списков без повторений: {[i for i in set(li_1 + li_2)]}')
print(f'Список, содержащий элементы общие для двух списков: {[i for i in li_1 if i in li_1 and i in li_2]}')
print(f'Список, содержащий только уникальные элементы каждого из списков: {[i for i in li_1 if i not in li_2] + [i for i in li_2 if i not in li_1]}') 
print(f'Список, содержащий только минимальное и максимальное значение каждого из списков: {[min(li_1), max(li_1), min(li_2), max(li_2)]}')
