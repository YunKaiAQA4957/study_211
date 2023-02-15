#zad3
class Converter:
    @staticmethod
    def MtE(num):
        return f'{num}(m) is {num*3.281}(ft) or {num*1.094}(yd)'
        
    @staticmethod
    def EtM(num):
        return f'{num}(ft) is {num/3.281}(m) or {num*30.48}(sm)'
        
print(Converter.EtM(2))
print(Converter.MtE(3))

#zad2
class Temp:
    counter = 0
        
    @staticmethod
    def F(t):
        Temp.counter += 1
        return f'{t}(C) is {t*1.8+32}(F)'
    
    @staticmethod    
    def C(t):
        Temp.counter += 1
        return f'{t}(F) is {(t-32)/1.8}(C)'
        
    @staticmethod
    def count():
        return Temp.counter
        
obj1 = Temp()
print(obj1.F(10))
print(obj1.C(10))

obj2 = Temp()
print(obj2.F(50))
print(obj2.C(50))

print(f'Number of temperature counts: {Temp.count()}')
