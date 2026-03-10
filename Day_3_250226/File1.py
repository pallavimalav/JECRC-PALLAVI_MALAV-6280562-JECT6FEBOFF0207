# print('hello world')
# print('hello pyhton')
# a, b = int(input()), int(input())
# print(a+b)
 
#  Example : 1:
#  input: nums = [2,7,11,15], target = 9
#  output : [0,1]
#  explanation: because nums [0] + nums[1] == 9, we return [0,1] 


def twoNum(coll,target):
   for i in range (len(coll)-1):
       for j in range(i+1, len(coll)):
            if coll[i] + coll[j] == target:
               return[i,j]
   return  -1

coll = [11,15,2,7]
target = 9
print(twoNum(coll,target))



