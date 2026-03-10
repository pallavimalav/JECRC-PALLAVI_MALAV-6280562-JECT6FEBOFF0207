'''
exception: 
-> unauthorized event.
-> flow of the execution of the program will be stopped.
-> after that, it won't execute the further code.

# syntax error

# exception handling approaches: 3 types of approaches.
1. specific eh
2. generic eh
3. default eh

# approaches to raise an error in the program.
3 types


# keywords:

1. try: 
2. except: 
3. finally: 
4. else: 

# what is try block ? :- 

-- inside try block we will put problem statement.
-- problem statement is a block of code, due to whuch we might get error.
-- output : error, error name, reason, line no..

# else block :-

-- it is an alternative of try-block.
-- if we find out any error inside try block, interpreter will move forward towards else block.
-- output: -> if code is correct(output)
-> if code is incorrect (error)

# except block (important) :-

-- we put actual solution for the error.
-- solution is resolution for error prone code.
-- due to except block, we can prevent the unauthorized event(errors).
--> purple/pink : exception
--> red : error(class)
--> purple : warning

# finally block :-

-- after getting error or after resolution, forcefully if we want to execute any particular
    block of code then, we use finally.

# exception handling approaches:

1. specific exception handling :
-- if we are aware of the error/exception then wew can go with specific.

try:
    problem
    statment
except ErrorName:
    resolution/
    solution code

-->


'''
'''
n1, n2 = 21, 0
try:
    # problem statement
    result = n1/n2
    print(result)
except ZeroDivisionError:
    # solution code
    print('Please do not choose 0 as the second number!')

print('Code after try except - 01')
print('Code after try except - 02')
print('Code after try except - 03')

'''

# try:
#     a, b, c = 1, 2
# except ValueError:
#     print('For performing MVC, number of variables should be equals to number of values!')

# try:
#     print(a, b, c)
# except NameError:
#     print('Identifiers are not there in the memory!')


'''
generic exception handling :- 
it is a type of eh approch in which there is no need to pass any particular class name, instead we can use parent "exception"
class called "Exception"  .

-- drawback :
using generic eh we cant handle keyboard interruption. 

'''

# try:
#     a, b, c = 1, 2
# except Exception:
#     print('For performing MVC, number of variables should be equals to number of values!')

# try:
#     print(a, b, c)
# except Exception:
#     print('Identifiers are not there in the memory!')



# try:
#     while True:
#      print(time.time())
# except Exception:
#     print('Loop got stopped!')

'''
-- Default Exception: 
it is a type of eh in which we can handle all types of errors or exceptions except "SynatxError".

'''


# import time
# try:
#     while True:
#      print(time.time())
# except:
#     print('Loop got stopped!')

'''
raise --> it is a keyword, which helps us to throw an error in-betweeen a program.

Exception Creation : 

1. custom exception, (raise)
2. user-defined exception, (raise)
3. assertion exception, (assert)
'''

'''
Custom Exception:
1. we use pre-built exception classes according to our requirement.

raise ValueError('message')

ValueError: message
'''
# num = 17
# if num >= 18:
#     print('Your are eligible for voting and driving!')
# else:
#     raise ValueError('Age should be greater than or equal to 18!')

'''
-- user defined exception:

it is a type of exception in which we can create our own exception classes based upon our own requirment. we can also provide names
to those classes according to our user classes

'''
# class MyException(Exception):
#     pass

# # raise MyException('This is my excpetion class!')

# n1, n2 = 10, 8
# if n2 == 0:
#     raise MyException('Second num cannot be zero')
# else:
#     print(n1 / n2)


'''
Assertion - exception:

assertion exception can be created by using one keyword called "assert".


assert <condition>, print(ERROR)
print(output)

'''
s = input('Enter a string:')
assert s == s[::-1], print('It is not a palindromic string!')
print('it is palindromic string!')

