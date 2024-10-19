pyramid_rows = 5
d_cell = "*"
w_cell = "#"

for i in range(pyramid_rows):

    #How to invert the pyramid

    d_cells_per_row = i + 1
    w_cells_per_row = pyramid_rows - d_cells_per_row

    row_version_1 = [
      w_cell * w_cells_per_row,
      d_cell * (d_cells_per_row + i),
    ]
    
    row_version_2 = (
        row_version_1 + [w_cell * w_cells_per_row]
    )       
    
    print(row_version_2)

    #print(*row_version_1,end='\n')

#white cell = w_cell = | |
#dark cell = d_cell = |x|
#pyramid rows = 3
#| || ||x| <-- row (i = 0) 
#| ||x||x| <-- row (i = 1)
#|x||x||x| <-- row (i = 2)