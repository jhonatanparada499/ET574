#01
n = []

#02
n.extend([2,4])
#03
print(n)

#04
n.extend([0,1,3])
n.sort()
#05
print(n)

#06
n.append(5)
#07
print(n)

#08
n.remove(0)
#09
print(n)

#10
removed_nums = [n.pop(n.index(2))]
print(n)
#11
print(removed_nums[0])

#12
removed_nums.append(n.pop(n.index(4)))
print(n)
#13
print(removed_nums[1])

#14
print(f'Sum of all removed numbers = {sum(removed_nums)}')

#15
n[0] = 100
n[-1] = 9.9
print(n)

#16
newNum = n.copy()

#17
n.clear()

#18
print(
    f'Original list = {n}',
    f'New list = {newNum}',
    sep='\n'
)

#19
del n