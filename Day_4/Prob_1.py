'''
Problem : 
calculate electricity bill based on units consumed. 

0-100 -> $5/unit
101-300 -> $7/unit
Above 300 -> $10/unit 

If bill > 5000 -> 5% discount
'''
# take the unit from user (int number).
# apply all the conditions and calculate the total bill amount.
# check another condition for applying discount.

units = int(input('Enter unit: '))
bill_amount = None

if units > 0:
    if units <= 100:
        bill_amount = units * 5
    elif 101 <= units <= 300:
        bill_amount = units * 7
    else:
        bill_amount = units * 10

        # Calculating discount
        if bill_amount > 5000:
            bill_amount = bill_amount * 0.95
            # F string --> string + expression
            print(f'Bill amount after discount: {bill_amount}')
else:
    print('Enter valid units!')
