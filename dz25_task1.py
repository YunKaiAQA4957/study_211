class Car:

    def __init__(self):
        self.model = input('Model: ') 
        self.year = int(input('Year: '))
        self.manuf = input('Manuf: ')
        self.engine = float(input('Engine: '))
        self.color = input('Color: ')
        self.price = int(input('Price: '))
        print('*'*40)
    
    def out_info (self):
        return f'Car - Model: {self.model}, Year: {self.year}, Manufacturer: {self.manuf}, V-Engine: {self.engine}, Color: {self.color}, Price: {self.price}.'
    
    def Model_car(self):
        return f'Model car: {self.model}'

    def Year_car(self):
        return f'Year car: {self.year}'

    def Manuf_car(self):
        return f'Manuf car: {self.manuf}'

    def Engine_car(self):
        return f'Model car: {self.engine}'

    def Color_car(self):
        return f'Color car: {self.color}'

    def Price_car(self):
        return f'Price car: {self.price}'    
    
        
            

obj = Car()
print(obj.out_info())
print(obj.Color_car())
print(f'Model: {obj.model}')