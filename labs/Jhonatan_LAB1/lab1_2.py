#lab1_2.py - Displays a Functional and Customizable Receipt - Jhonatan Parada Torres

#Customization
 
tab = "\t\t" #The space or distance between the columns 
line_divider = ["-----","-----"] #The characters for the lines between rows  
header = ["Items","Price"] #The titles displayed at the top of each column(This model only supports 2 columns)

#Items

final_price = 0
items = [
    header,
    line_divider,
    ["Apple",1.75],
    ["Banana",2.25],
    ["Cherry",3.5],
    #Add more items here following the format list, such as ["your item", "the price of it"],
    line_divider,
    ["Total",1]
]

#Calcaulation and Display 

for item in items:
    #Identifies the prices of the items
    item_price = item[1] if item[1] and isinstance(item[1],(int,float)) else 0
 
    if item_price:
        if item != items[-1]:
            #Adds the prices of the items to the final price if it hasn't reached the last element of the list
            final_price += item_price
        else:
            #The final price is assigned to the last element of the receipt, being "Total" in this case
            items[-1][1] = final_price

        #Concatenates the '$' symbol to all the numbers of the receipt
        item[1] = f"${item[1]}"

    print(*item,sep=tab)
    
    