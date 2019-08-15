## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

for row in grid:
    xcounter_row = 0
    for item in row:
        if item == 'X':
            xcounter_row += 1

    if xcounter_row %2 ==0:
        row.append('0')
    else:
        row.append('X') 


maxCol = len(grid[0])
maxRow = len(grid)
new_row =[]

for y in range(maxCol):
    x_count = 0
    for x in range(maxRow):
        if grid[x][y] == 'X':
            x_count += 1
    if x_count %2 ==0:
               new_row.append('0')
    else:
            new_row.append('X') 
       
#print(new_row)

grid.append(new_row)

# print(grid)
        
counter = 0
for list in grid:
    print(list)
    counter += 1

coordinates =input ('enter coordinates of card to flip in form "(x , y)" ')

#Now need to test whether input is valid and give error messages accordingly.
#Then need to flip the card at appropriate coordinates and then print grid again.

# first step is to add colum 6 and row 6

# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)

# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)