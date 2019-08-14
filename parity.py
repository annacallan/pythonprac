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

print(grid)

for y in range(6):
    for x in range(5):
        print(grid[x][y])
    print("\n")





# first step is to add colum 6 and row 6

# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)

# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)