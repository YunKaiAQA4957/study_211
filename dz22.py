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

print('*'*40)
input('Для выхода нажмите Enter')