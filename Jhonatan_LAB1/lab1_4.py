#lab1_4.py - Discounted price - Jhonatan Parada Torres

initial_price = 99.99
discountPersent = 25
markdown = discountPersent / initial_price * 100
final_price = initial_price - markdown

#The final price is being round to 2 decimal places using formatted string literals
print(f"Price = {final_price:.2f}")
