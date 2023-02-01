class Animal:
    COUNT = 0
    def __init__(self, name='', type_of_animal='', age=''):
        self.name = name
        self.type_of_animal = type_of_animal
        self.age = age
        Animal.COUNT +=1

dog = Animal('Yun_Kai', 'dog', 3)
cat = Animal('Motya', 'cat', 11)
bird = Animal('Kesha', 'bird', 5)
horse = Animal('Plotva', 'horse', 6)
animal_dict = Animal()

print(dog.__dict__)
print(cat.__dict__)
print(bird.__dict__)
print(horse.__dict__)
print(animal_dict.__dict__)
print(Animal.__dict__)
print(f'Количество животных {Animal.COUNT}')

print('*'*40)
input('Для выхода нажмите Enter')