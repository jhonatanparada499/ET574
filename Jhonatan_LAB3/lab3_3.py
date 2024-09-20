# README 
# For this exercise I'm using for loops, dictionarys, the method values()
# and try statements

# LOGIC
# dictionary is going to contain the values the user inputs;
# the for loop is going to iterate over dictionary at the same
# time it saves the date into dictionary;
# the try statement inside the for loop is going to handle errors
# in case the user inputs anythin that is not an integer;

# After the try statement, I used the list function to save only
# the values of the dicitonary in a new variable called non_sorted_values;

# Since one of the requirements of Lab #3 is to include the 
# max and min built-in function, I give "first" item the min
# value and "third" item the max value of non_sorted_values 

# (This code is not scalable and only works with 3 items in dictionary,
# meaning that if one adds more items to dictionary, it will not work);

# Finally the last for loop compares every value of the non_sorted-
# _list with the values of the dictionary, and assigns the only
# number available that is not the minimum and not the maximum to
# the "second" item of the dictionary. 

error_message = "Exceptions: Invalid Input"

dictionary = {
    "first": 0,
    "second": 0,
    "third": 0
}

for key,value in dictionary.items():
    try:
        dictionary[key] = int(
            input(
                f"Please enter the {key} integer: "
            )
        )
    
    except ValueError:
        print(error_message)
        exit

dict_values = dictionary.values()

non_sorted_values = list(dict_values)

dictionary["third"] = max(non_sorted_values)
dictionary["first"] = min(non_sorted_values)

for value in non_sorted_values:
    if value != dictionary["first"] and value != dictionary["third"]:
        dictionary["second"] = value
        sorted_values = list(dict_values)

print("Before sorting:",*non_sorted_values)
print("After sorting:",*sorted_values)

