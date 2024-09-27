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

myInfo.reverse()
print(myInfo)

#E
myInfo.reverse() #using the original list
sprtor = ' <<<< ' #separator

# print(" ".join(myLst))
# Error: variable myLst does not exist, it should be
# myInfo. Second error is that the join method does
# not support int items in the iterable 

# To accomplish the required ouput I see 2 solutions:

# The first one would require to use a loop to convert all
# the items in the list to string and then use the join method.
# The second one is simplier but it does not use the join
# method. 

# Second solution 
print(*myInfo, sep=sprtor) # '*' at the beggining breaks down the list


# First solution
myInfo = [str(item) for item in myInfo] # list comprehension
print(sprtor.join(myInfo))
