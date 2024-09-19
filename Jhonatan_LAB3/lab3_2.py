string = input("Please enter a string: ")

output = (
    f"Original Text: {string}",
    f"First Letter: {string[0]}",
    f"Last Letter: {string[-1]}",
    f"Reversed Text: {string[::-1]}"
)

print(*output,sep='\n')