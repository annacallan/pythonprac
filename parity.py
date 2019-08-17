## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

# first step is to add colum 6 and row 6

# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)

# output the grid with the flipped card


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


max_col = len(grid[0])
max_row = len(grid)
new_row =[]

for y in range(max_col):
    x_count = 0
    for x in range(max_row):
        if grid[x][y] == 'X':
            x_count += 1
    if x_count %2 ==0:
        new_row.append('0')
    else:
        new_row.append('X') 
       
#print(new_row)

grid.append(new_row)

#print(grid)
 
def print_grid():
    counter = 0
    for list in grid:
        print(list)
        counter += 1

print_grid()

def enter_coordinates():
    while True:
        coordinates =input ('enter coordinates of card to flip in form "x,y" ')
        if '.' in coordinates:
            print('Whoops that\'s not correct, try again! Enter two numbers 0-5 seperated by a comma')
            continue
        elif ',' not in coordinates: 
            print('Whoops that\'s not correct, try again! Enter two numbers 0-5, don\'t forget the comma')
            continue
        #elif '(' or ')' in coordinates:    
         #   print('Whoops that\'s not correct, try again! Enter two numbers 0-5 seperated by a comma. No brackets are required')
          #  continue
        elif ',' in coordinates: 
            list_coord = coordinates.split(",")
            tuple_coord = tuple(list_coord)
            # print(tuple_coord)

            x = int(tuple_coord[0])
            y = int(tuple_coord[1])

            if x in range(0,6) and y in range(0,6):
                return (x,y)  
            else:
                print('Please enter two values 0-5 seperated by a comma')
                

                
x, y = enter_coordinates()

# print(grid[x][y])

def card_flip(x, y):
    if grid[x][y] == 'X':
        grid[x][y] ='0'
    else:
        grid[x][y]='X'


card_flip(x, y)
# print(grid[x][y])

print_grid()


## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)

grid1 = [
    ['0','X','0','X','X'],
    ['X','X','X','0','0'],
    ['X','0','0','0','X'],
    ['0','X','X','0','X'],
    ['X','0','X','X','X'],
]

grid2 = [
    ['0','X','0','X','X'],
    ['X','X','X','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','0','X'],
    ['X','0','X','X','X'],
]

max_col = len(grid1[0])
max_row = len(grid1)

for y in range(max_col):
    x_count = 0
    for x in range(max_row):
        if grid1[x][y] != grid2[x][y]:
            print((x, y))
        else:
            continue


