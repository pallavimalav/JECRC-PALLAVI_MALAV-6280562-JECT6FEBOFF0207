# 1. input : [10,2.2,5,'Hello', [100,200],99.9]
# output : 99.9 // maximum
# type(i) in [int, float]

# 2. input : {'a':1, 'b':2, 'c':3, 'd':4}
# output : {1:'a', 2:'b', 3:'c', 4:'d'}

# 3. input : ('Hello', 'Hi', 20, 40.2, 9.6, [1,2], 'Python', 'JECRC', (1,2,3))
# output : {'Hello':'1', 'Hi':'Hi', 'Python':'PN', 'JECRC':'C', (1,2,3):2}

# take inputs from the user and check user inputs
# don't use any inbuilt functions 


# 1 
coll = [1, 'Hello', 3.2, [1,2,3]]
max = coll[0]

for i in coll:
   if type(i) in [int, float]:
    if i > max:
    max = i
    print(max)


# 2
coll = {'a':1,'b':2 }
new_coll = {}
for i in coll:
    new_coll[coll(i)] = i
print(new_coll)    


# 3
coll = eval(input('Enter a collection:'))
new_coll = {}
for i in coll:
   if type(i) in [str, tuple]:
      if len(i) % 2 == 0:
         new_coll[i] = i[0] + i[-1]
      else:
         new_coll[i] = i[len(i)//2]
print(new_coll)


# whenever python interpreter will encounter break keyword, it will simply stop its execution on this particular line and make the interpreter to go outside of the loop. in future,
# control will never go inside the same loop again.

coll =[1,1.2,3,4,5,'Hi']
i, flag = coll[0] , True

for i in coll:
   type(i) == type(j):
   flag = True
else:
   flag = False
   
   if flag:
      print('Homogenous Collection!')
   else:
      print('Hetrogenous Collection!')

      
      

