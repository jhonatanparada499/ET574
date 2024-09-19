celebrate = "hispanic heritage month"
celebrate = celebrate.title()

#Index, Slicing String Methods

result_1 = (
    f"'{
        celebrate[
            celebrate.index("s"):
            celebrate.index("n") + 1
        ]
    }'"
)

result_2 = (
    celebrate[
        celebrate.index("o"):
        celebrate.rindex("n") + 1
        ]
)

result_2 = result_2.upper()

#Careful when there is more than 
#variable[x:y]
#y >= x
#variable[0:1] = variable[:1]
#varible[1:2]

print()
