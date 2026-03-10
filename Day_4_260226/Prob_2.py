'''
loan approval system 

" Problem:
loan approved if:

salary > 25,000
CIBIL score > 700 
if salary > 50,000 & CIBIL > 750 -> instant approval (skip)

otherwise -> rejected"
'''
salary = int(input("Enter salary: "))
CIBIL_score = int(input("Enter CIBIL score: "))

if salary > 25000 and CIBIL_score > 700:
    print("Instant approved!")

    if salary > 50000 and CIBIL_score < 700:
        print("Instant Approval!")
        print("Loan Approved1")
    else:
        print("Loan will be approved after background verification!")
else:
        print("Rejected!")

