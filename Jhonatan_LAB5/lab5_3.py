mult_of_4 = [num*4 for num in range(0,10 + 1)]
sec_list = []

for num in mult_of_4: sec_list.append(num // 2)

thir_list = sec_list[:]

for num in thir_list:
    num_index = thir_list.index(num)
    thir_list[num_index] = num // 2 

print(mult_of_4)
print(sec_list)
print(thir_list)