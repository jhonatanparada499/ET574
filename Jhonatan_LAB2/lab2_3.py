pyramid_height = 8

for i in range(pyramid_height):
    print(" " * (pyramid_height - (i + 1)),"*" * (i + (i + 1)),sep='',end='\n')


