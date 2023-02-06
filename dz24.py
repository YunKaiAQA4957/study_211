class Animal:

    def __init__(self, name, typeAN):
        self._name, self.__typeAN = "noname", "noname"
        self.set_name(name)
        self.set_typeAN(typeAN)

    def info_animal(self):
        print(f'Кличка животного: {self._name}\n'
              f'Вид животного: {self.__typeAN}')

    def get_name(self):
        return self._name

    def set_name(self, value):
        if self.is_valid(value):
            self._name = value
        else:
            print("Не удалось записать параметр")

    def get_typeAN(self):
        return self.__typeAN

    def set_typeAN(self, value):
        if self.is_valid(value):
            self.__typeAN = value
        else:
            print("Не удалось записать параметр")

    @staticmethod
    def is_valid(value):
        return isinstance(value, str) and not value.isdigit() and len(value) > 0

animal = Animal('Yun-Kai', 'dog')
animal.info_animal()
animal.set_name(10)
animal.set_typeAN('Horse')
animal.set_name('Boris')
print(animal.get_name())

print(animal.get_typeAN())