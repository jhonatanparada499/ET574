even_nums = [num for num in range(0, 101, 2)]

print(even_nums[:5])
print(even_nums[-5:])
print(even_nums[even_nums.index(44) : even_nums.index(88) + 1])
