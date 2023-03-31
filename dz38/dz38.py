class Employee:
   
    def load_list_empl():
        try:
            Employee.load_list_empl.path_dir = input('Укажите файл со списком сотрудников в формате txt: ')
            Employee.load_list_empl.tmp_li = []
            with open(Employee.load_list_empl.path_dir, 'r', encoding='utf-8') as list_empl:
                print('\n' + '+'*20 + ' Список загружен ' + '+'*20 + '\n')
                Employee.load_list_empl.li_num = {}
                for idx, line in enumerate(list_empl, 1):
                    Employee.load_list_empl.li_num[idx] = line.split(' | ')
                    Employee.load_list_empl.last_idx = idx
                    print(f'{idx}. {line}')
        except:
            print('\n' + '+'*20 + ' Список не загружен ' + '+'*20 + '\n')
            print('Такого файла не существует!')
            print('\n' + '+'*20 + ' Загрузка списка сотрудников ' + '+'*20 + '\n')
            return Employee.load_list_empl()



    def menu_empl_add():
        new_emp = input('Введите ФИО сотрудника: ')
        new_emp_age = int(input('Введите возраст сотрудника: '))
        Employee.load_list_empl.li_num[Employee.load_list_empl.last_idx + 1] = [f'{new_emp}',f'{new_emp_age}\n']
        return Employee.menu()
    
    def menu_empl_edit():
        try:
            empl_idx = int(input('Введите индекс сотрудника: '))
            if empl_idx in Employee.load_list_empl.li_num:
                new_emp = input('Введите новое ФИО сотрудника: ')
                new_emp_age = int(input('Введите новый возраст сотрудника: '))
                Employee.load_list_empl.li_num[empl_idx] = [f'{new_emp}',f'{new_emp_age}\n']
            return Employee.menu()
        except KeyError:
            print('Не верно указан индекс')
    
    def menu_empl_remove():
        try:
            empl_idx = int(input('Введите индекс сотрудника для удаления: '))
            if empl_idx in Employee.load_list_empl.li_num:
                Employee.load_list_empl.li_num[empl_idx] = ['Удалён', 'Удалён\n']
            return Employee.menu()
        except KeyError:
             print('Не верно указан индекс: ')
    
    def menu_empl_search_last_name():
        ln_srch = input('Введите фамилию сотрудника: ')
        for key, value in Employee.load_list_empl.li_num.items():
            i, j = value
            if ln_srch in str(i):
                print('\n' + '+'*20 + ' Найдено совпадение ' + '+'*20 + '\n')
                src_hist = f'{key}. {i} - возраст: {j}'
                Employee.load_list_empl.tmp_li.append(src_hist)
                print(src_hist)
        return Employee.menu()
    
    def menu_empl_out():
        print('\n' + '+'*20 + ' Список сотрудников ' + '+'*20 + '\n')
        for key, value in Employee.load_list_empl.li_num.items():
            i, j = value
            print(f'{key}. {i} - возраст: {j}')
        return Employee.menu()

    def menu_empl_search_age():
        age_srch = input('Введите возраст сотрудника: ')
        print('\n' + '+'*20 + ' Найдено совпадение ' + '+'*20 + '\n')
        for key, value in Employee.load_list_empl.li_num.items():
            i, j = value
            if age_srch in str(j):
                src_hist = f'{key}. {i} - возраст: {j}'
                Employee.load_list_empl.tmp_li.append(src_hist)
                print(src_hist)
        return Employee.menu()
    

    def menu_empl_search_letter():
        try:
            ltr_srch = input('Введите первую букву фамилии: ').upper()
            if len(ltr_srch) > 1 or ltr_srch.isdigit():
                raise AssertionError
            
            print('\n' + '+'*20 + ' Найдено совпадение ' + '+'*20 + '\n')
            for key, value in Employee.load_list_empl.li_num.items():
                i, j = value
                if ltr_srch == str(i[0]):
                    src_hist = f'{key}. {i} - возраст: {j}'
                    Employee.load_list_empl.tmp_li.append(src_hist)
                    print(src_hist)
            else:
                print('\n' + '+'*20 + ' Совпадение не найдено ' + '+'*20 + '\n')
        
        except AssertionError:
            print('\n' + '+'*20 + ' Ошибка ' + '+'*20 + '\n')
            print('Ошибка ввода!\n')
            print('+'*48)
            return Employee.menu_empl_search_letter()
        
        return Employee.menu()
    
    def menu_empl_save():
        with open(Employee.load_list_empl.path_dir, 'w+', encoding='utf-8') as list_empl:
            for _, value in Employee.load_list_empl.li_num.items():
                i, j = value
                list_empl.write(f'{i} | {j}')
        print('\n' + '+'*20 + ' Изменения сохранены в фаил ' + '+'*20 + '\n')
        return Employee.menu()
    
    def menu_empl_exit():
        with open(Employee.load_list_empl.path_dir, 'w', encoding='utf-8') as list_empl:
            for _, value in Employee.load_list_empl.li_num.items():
                i, j = value
                list_empl.write(f'{i} | {j}')
        print('\n' + '+'*20 + ' Выход из программы ' + '+'*20 + '\n')

    def menu_srch_save():
        with open("srch.txt", 'w+', encoding='utf-8') as srch_empl:
            for i in Employee.load_list_empl.tmp_li:
                srch_empl.write(f'{i}')
            Employee.load_list_empl.tmp_li = []
        return Employee.menu()

    def menu():
        print('\n' + '+'*20 + ' Выбор действия ' + '+'*20 + '\n')
        print(f'1:Ввод данных\n'
               '2:Редактирование данных сотрудника\n'
               '3:Удаление сотрудника\n'
               '4:Поиск сотрудника по фамилии\n'
               '5:Вывод информации обо всех сотрудниках\n'
               '6:Вывод информации о сотрудниках указанного возраста\n'
               '7:Вывод информации о сотрудниках по начальной букве фамилии\n'
               '8:Сохранить изменения в фаил\n'
               '9:Сохранить результат поиска в отдельный фаил\n'
               '*:Выход из программы\n'
               )
        
        pm = input('Выбирите действие: ')
        
        if pm == '1':
            Employee.menu_empl_add()
        elif pm == '2':
            Employee.menu_empl_edit()
        elif pm == '3':
            Employee.menu_empl_remove()
        elif pm == '4':
            Employee.menu_empl_search_last_name()
        elif pm == '5':
            Employee.menu_empl_out()
        elif pm == '6':
            Employee.menu_empl_search_age()
        elif pm == '7':
            Employee.menu_empl_search_letter()
        elif pm == '8':
            Employee.menu_empl_save()
        elif pm == '9':
            Employee.menu_srch_save()
        elif pm == '*':
            Employee.menu_empl_exit()
        else:
            print('\n' + '+'*20 + ' Ошибка ' + '+'*20 + '\n')
            print('Неверный ввод!')
            return Employee.menu()
                   
print('\n' + '+'*20 + ' Загрузка списка сотрудников ' + '+'*20 + '\n')
Employee.load_list_empl()

Employee.menu()

print('\n' + '+'*20 + ' END ' + '+'*20 + '\n')
input('Enter to exit')