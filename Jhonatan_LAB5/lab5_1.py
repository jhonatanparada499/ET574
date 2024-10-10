# Universal Variables
start_num, stop_num  = 1, 11
nums_range = range(start_num, stop_num)
nums_list = list(nums_range)

odd_nums = nums_list[::2]
cubed_nums = [num**3 for num in nums_range]

print(odd_nums)# A
for num in cubed_nums: print(num)# B

for num in cubed_nums: print(num, end='|') 
else: print() # C