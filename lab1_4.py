#lab1_4.py - Discounted price - Jhonatan Parada Torres

price = 99.99
discountPersent = 25
markdown = discountPersent / price * 100
price = price - markdown

print(f"Price = {price:.2f}")
