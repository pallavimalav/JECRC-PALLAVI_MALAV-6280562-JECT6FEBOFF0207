'''
encapsulation:
it is used to provide security to the data(data means variable or properities and methods present inside class.)

How to provide security to a data?
to provide security we have to used access specifiers.
1. public,
2. private,
3. protected(Soft Barrier)


access specifier: 
it describes who can access the class memebers (properties & methods.)
'''

# Example for access specifier.
'''
class Temp:
    a,b,*c,d = 'HELLO'

    def greeting(self):
        print('Good Afternoon user:)')

class C2(Temp):
    pass
    '''

# Protected Access Specifier:
'''
class Temp:
    # single underscore is known as soft barrier(_)
    _a = 10
    _b = 'I LOVE PYTHON!'

obj = Temp()
print(obj._b)
print(obj._a)
'''

# Private
'''
class Temp:
    __a = 100  # update to 0123456789

    def __status(self):
        print('Class name is Temp!')

obj = Temp()
# print(obj.__a)
# obj.__status()
'''

'''
how to access them :
1. by using synatx,
2. get & set method,
3. by using @property decorator(setter).

'''
#  by using synatx
'''
obj_name/class_name._CN__prop_name/__method_name (Accessing)
obj_name/class_name._CN__MemberName = new_method (Modifing)

'''
'''
print(obj._Temp__a) #100 --> '0123456789' update the value or either update method definition.
print(Temp._Temp__a)
obj._Temp__status()

def new_method():
    print('Method definition got changed!')

obj._Temp__a = '0123456789'
obj._Temp__status = new_method   #new_method()
print(obj._Temp__a)
obj._Temp__status()  #obj._Temp__status()


# by using get & set method
'''
'''
class Temp:
    __a = 100

    def __status(self):
        print('Class name is Temp!')

    def get(self):
        print(self.__a)

    def set(self, new_val):
        self.__a = new_val
obj = Temp()
obj.get()
obj.set(1)
obj.get()
print(obj._Temp__a)
'''

# by using @property decorator
class Temp:
    __a = 10

    @property
    def get(self):
        print(self.__a)

    @get.setter 
    def set(self, new_val):
        self.__a = new_val

obj = Temp()
obj.get
obj.set = 10000
obj.get
print(obj._Temp__a)

