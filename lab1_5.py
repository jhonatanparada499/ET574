#lab1_5.py - Miles per Galon a car averaged between two fillings - Jhonatan Parada Torres

#Customization
initial_mile = 23456
last_mile = 23678
gallon_used = 10
rounded_answer = 3

#Calculation
distance_traveled = last_mile - initial_mile
miles_per_galon = distance_traveled / gallon_used

answer = round(miles_per_galon, rounded_answer)

print(
    "How many miles per gallon did the car average between two fillings?\n"
    f"Answer: {answer} Miles/Gallon"
)