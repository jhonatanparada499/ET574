#README
#The reason why I'm using the try statement is because it allows me to 
#handle or manage potential errors without crashing the program.
#I avoided using a loop this time to stay in track with the learned topics

error_message = "Exceptions: Invalid Input"

try:
    bill = float(input("Enter the amount of the bill: "))
    
    try:
        percentage = int(input("Enter the percentage of the tip: "))

        tip = bill * (percentage / 100)

        print(f"Tip: ${tip:.2f}")

    except ValueError:
        print(error_message)

except ValueError:
    print(error_message)