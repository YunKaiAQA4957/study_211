class Func:
    
    def composition(li):
        x = 1
        for i in li:
            x *= i
        return f'Произведение списка: {x}'

    def min(li):
        return f'Минимальное значение: {min(li)}'

    def count_li(li):
        count = 0
        l = []
        for i in li:
            if i > 1:
                for j in range(2, i):          
                    if (i % j) == 0:
                        break
                else:
                    count += 1
        return f'Количество простых чисел: {count}'
    
    def delet(n, li):
        count = 0
        for i in li:
            if i == n:
                del li[li.index(i)]
                count += 1
        return f'Количество удаленных чисел: {count}'

    def double_li(li1, li2):
        return f'Объедененный список: {li1 + li2}'

    def degree(d, li):
        n_li = []
        for i in li:
            n_li.append(i ** d)
        return f'Новый список: {n_li}'   

        
print(Func.composition([1,2,3,4]))
print(Func.min([1,2,3,4]))
print(Func.count_li([1,2,3,4]))
print(Func.delet(2, [1,2,2,3,4]))
print(Func.double_li([1,2,3,4],[5,6,7,8]))
print(Func.degree(5, [1,2,3,4]))