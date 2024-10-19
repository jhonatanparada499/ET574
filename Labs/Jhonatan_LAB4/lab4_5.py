#A
myInfo = ['apple','banana','cherry']

# print(myInfo[3])
# Error: index 3 do not exist in myInfo

print(myInfo[2]) #or myInfo[-1]

#B
# newInfo = myInfo
# Logical Error: any changes in myInfo will be reflected in newInfo

newInfo = myInfo.copy()

#C
myInfo = 'sea'

# myInfo[0] = 'p'
# Error: strings do not support item assignment

myInfo = myInfo.replace('s','p')

print(myInfo)

#D
myInfo = [1, "two",'three', 4]

# print(myInfo[-1:-4])
# Logical Error: if the second value of slicing is less
# or equal than the first value, it will print an empty list
# because does not go backwards.

myInfo.reverse() # or myInfo[::-1]
print(myInfo)

#E
myInfo = [1,'two','three',4] #using the original list
sprtor = ' <<<< ' #separator

# print(" ".join(myLst))
# Error: variable myLst does not exist, it should be
# myInfo. Second error is that the join method does
# not support int items in the iterable 

# To accomplish the solution:

# Convert all elements of the list to string,  
# then I will use the join method.

myInfo[0] = str(myInfo[0])
myInfo[-1] = str(myInfo[-1])

print(sprtor.join(myInfo))

# another solution 
# print(*myInfo, sep=sprtor) # '*' at the beggining breaks down the list
# without * = print(['a','b','c']) with * = print(a,b,c)
