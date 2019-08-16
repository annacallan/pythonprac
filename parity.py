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



# first step is to add colum 6 and row 6

# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)

# output the grid with the flipped card



## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)

# OR do I want to unpack eack list and examine individually?

# def compare_lists(grid1, grid2):
#     # Let's initialize our index to the first element
#     # in any list: element #0.
#     item = 0

#     while item < len(grid1) and item < len(grid2):
#         if grid1[item] != grid2[item]:
#             # If any two elements are not equal, say so.
#             return False

#     return True