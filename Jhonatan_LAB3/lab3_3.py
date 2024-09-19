#README 
error_message = "Exceptions: Invalid Input"

# integers = {
#     "first": 0,
#     "second": 0,
#     "third": 0
# }

integers = [
    ["first"],["second"],["third"]
]

for integer in integers:
    try:
        integer = integer + [
            int(
                input(f"Please enter the {integer} integer")
            )
        ]
        
        # integers[integer] = int(
        #     input(f"Please enter the {integer} integer: ")
        # )
    except ValueError:
        print(error_message)
        exit

# before_sorting = [integers.values()]
# after_sorting = before_sorting[::-1]

min_integer = min(integers) #Second
max_integer = max(integers) #"First"

print(integers)

# print(
#     "Before sorting:", *before_sorting, "\n"
#     "After sorting:", *after_sorting
# )