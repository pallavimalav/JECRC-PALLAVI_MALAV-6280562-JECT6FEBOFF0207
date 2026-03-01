# elif statement
# when you have multiple conditions ; multiple statement blocks;
# at least one if condition should be there


# wap in python to take a character from the user and check wether it is a vowel or, consonent or, digit or, special character.
'''
1. take a character from the user
2. apply the conditions one by one
''' 


    ch = input('Enter a character: ')   # user enters one character

if ch in 'aeiouAEIOU':
    print('Vowel!')
elif ch in '0123456789':
    print('Digit!')
elif ch in '!@#$%^&*()':
    print('Special character!')
elif ch in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print('Consonant!')
else:
    print('Invalid input!')

