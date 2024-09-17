pyramid_rows = 5

#0,1,2,3,4...
#10,9,8,7...

for i in range(pyramid_rows):
    
    #0,1,2,3,4,5

    #white cell = w_cell = | |
    #dark cell = d_cell = |x|
    #pyramid rows = 3
    #| || ||x| <-- row (i = 0) 
    #| ||x||x| <-- row (i = 1)
    #|x||x||x| <-- row (i = 2)
    
    w_cell = " "
    d_cell = "*"

    w_cells_per_row = pyramid_rows - (i + 1) 
    d_cells_per_row = i + (i + 1)

    row = [
        w_cell * w_cells_per_row,
        d_cell * d_cells_per_row
    ]        

    print(*row,sep='',end='\n')


