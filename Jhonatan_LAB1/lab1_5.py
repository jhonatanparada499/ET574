#lab1_5.py - Miles per Galon a car averaged between two fillings/
# - Jhonatan Parada Torres

#Customization
initial_mile = 23456
last_mile = 23678
gallon_used = 10

#Calculation
distance_traveled = last_mile - initial_mile
answer = distance_traveled / gallon_used

#This line can be improved
print(
    f"Distance Traveled: {distance_traveled} Miles\nGallon Used: {gallon_used} Gallon(s)\n"
    "How many miles per gallon did the car average between two fillings?\n"
    f"Answer: {answer:.3f} Miles/Gallon"
)