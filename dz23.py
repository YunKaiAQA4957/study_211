class Animal:
    COUNT = 0
    def __init__(self, name='', type_of_animal='', age=''):
        self.name = name
        self.type_of_animal = type_of_animal
        self.age = age
        Animal.COUNT +=1

    def get_info(self):
        return f'{self.type_of_animal}:\n -Кличка животного: {self.name},\n -Возраст животного: {self.age}\n'

dog = Animal('Юн-Кай/Yun-Kai', 'Собака/Dog', 3)
cat = Animal('Мотя/Motya', 'Кошка/Cat', 11)
bird = Animal('Кеша/Kesha', 'Птица/Bird', 5)
horse = Animal('Плотва/Plotva', 'Лошадь/Horse', 6)
# animal_dict = Animal()

print(dog.__dict__)
print(cat.__dict__)
print(bird.__dict__)
print(horse.__dict__)
# print(animal_dict.__dict__)

print(Animal.__dict__)

print(Animal.get_info(dog))
print(Animal.get_info(cat))
print(Animal.get_info(bird))
print(Animal.get_info(horse))

print(f'Количество животных {Animal.COUNT}')





print('*'*40)
input('Для выхода нажмите Enter')