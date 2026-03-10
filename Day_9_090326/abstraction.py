'''
Abstraction : Hiding the internal implementation and showing only functionality to the end user.

Abstract Method: 
if a method/functionality consists of only declaration not definition then it will be called as 'Abstract Method'.

Abstract Class:
if a class consists of atleast one abstract method then it will be called as abstract class.

Concret class: 
if a class doesnt have even a single abstract method. / zero(0) abstract method.

abc :module
ABC : abstract base class

'''
from abc import ABC, abstractmethod

class ATM(ABC):   #abstract class
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM): # concret class
    def generate_pin(self):
        print('it is used to generate atm pin')

    def forget_pin(self):
        print('not able to remember the pin, then forget now!')

    def check_bal(self):
        print('no balance is available in your account!')

    def deposit(self):
        print('save your money by giving it to me!')

    def withdraw(self):
        print('do not withdraw the money please!')

obj = SBI_ATM()
obj.generate_pin()
obj.check_bal()
obj.forget_pin()
obj.deposit()
obj.withdraw()



        

    
