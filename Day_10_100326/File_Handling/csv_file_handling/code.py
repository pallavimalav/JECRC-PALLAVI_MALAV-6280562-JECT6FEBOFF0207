import csv 
from datetime import date

file = open('expense.csv', 'a+', newline='')
w = csv.writer(file)
# r = csv.reader(file)
# file.seek(0)

# print(list(r))
w.writerow(['DATE', 'CATEGORY', 'AMOUNT']) # coloumn
w.writerows(
    [
        [date.today(), 'Travel', 12000],
        [date.today(), 'Food', 5000],
        [date.today(), 'Entertainmen', 9000], 
    ]
)
file.close()

