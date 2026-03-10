'''
-- operator overloading: it is a phenomenon of making the opertaors to work on user-defined data types by invoking
respective magic methods.

-- Magic Method/Dundar: it is a special type of methods in which double undeescores will be there at the starting or ending 
of the method's name.

-- example: 
1. __add__,
2. __sub__,
3. __mul__,
4. __floordiv__,
5. __truediv__ 
6. __mod__

-- if we do not use operator overloading, then what will happen ?
for using operators inside user defined data types, we have to use opertaor overloading.


-- syntax:
class ClassName:
    def __init__(self, val):
      self.val = val

    def __add__(self, ano_obj):
        return self.val + anp_obj.val

obj1 = ClassName(val1)
obj2 = ClassName(val2)
print(obj1 + obj2) ## obj1.__add__(obj2)

'''

class MyDT:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def __add__(self, ano_obj):
        sum = self.val
        for i in ano_obj:
            sum += i.val
            return MyDT(sum)

        # for addition

    def __add__(self, ano_obj):
        return self.val + ano_obj.val
    
# 

    
    def add(self, *args):
        sum = self.val
        for i in args:
            sum += i.val
        return sum
    
    #  for subtraction
    
    def __sub__(self, ano_obj):
        return self.val - ano_obj.val
    
    def __sub__(self, ano_obj):
        subtraction = self.val
        for i in ano_obj:
            subtraction -= i.val
            return MyDT(subtraction)

    
    # 
    

    def sub(self, *args):
        subtract = self.val
        for i in args:
            subtract -= i.val
        return subtract
    
    # for multiplication
    

    def __mul__(self, ano_obj):
        return self.val * ano_obj.val
    

    def __mul__(self, ano_obj):
        mulitplication= self.val
        for i in ano_obj:
            mulitplication *= i.val
            return MyDT(mulitplication)

    # 
    
    def mul(self, *args):
        multiply = self.val
        for i in args:
            multiply *= i.val
        return multiply
    
    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val
    
    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val
    
    def __mod__(self, ano_obj):
        return self.val % ano_obj.val
    
    
    # def add_nums(*args):
    # print(args , type(args))
    # sum = 0 
    # for i in args :
        # sum += i 
    # print(f'Adiition : {sum}')
# add_nums()        
# add_nums(1,2,3,4,5)


# add = MyDT(100) + MyDT(200) + MyDT(300) + MyDT(400) + MyDT(500)
# print(MyDT.add(MyDT(100), MyDT(200), MyDT(300), MyDT(400), MyDT(500)))
print(MyDT(10) + MyDT(20) + MyDT(30))


print(MyDT.sub(MyDT(50), MyDT(40), MyDT(30), MyDT(20), MyDT(10)))

print(MyDT(10) - MyDT(20) - MyDT(30))

print(MyDT.mul(MyDT(10), MyDT(20), MyDT(30), MyDT(40), MyDT(50)))

print(MyDT(10) * MyDT(20) * MyDT(30))

print(MyDT(10) * MyDT(20))
print(MyDT(20) // MyDT(40))
print(MyDT(50) / MyDT(10))
print(MyDT(5) % MyDT(2))






    