# Lists

backpack = []
# print(backpack)

backpack = [
    'drink bottle',
    'yoghurt',
    'headphones',
    'laptop',
]

backpack.append('blueberries')
backpack.append('book')
backpack.append('pythons')

backpack[0] = 'lunchbox'

# name = 'hayley'
# print(name[0])
# name[0] = 'c' # doesn't work
# print(name)

# print(backpack)

# ['lunchbox', 'yoghurt', 'headphones', 'laptop', 'blueberries', 'book', 'pythons']

# for index,item in enumerate(backpack):
#     print(index, item)

# print()

# counter = 0
# for item in backpack:
#     print(counter, item)
#     counter = counter + 1

# print()

# counter = 0
# while counter < len(backpack):
#     print(counter, backpack[counter])
#     counter = counter + 1

# range()

# output the numbers 1 to 10 using a for loop
# output the numbers 1 to 10 using a while loop

# print('for loop')
# for num in range(1, 11):
#     print(num)

# print()
# print('while loop')
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# Tuples

person = ('hayley', 'awesome')
print(person)
person[0] = 'lj'

def cats():
    return ('boris', 'larry', name)

cat1, cat2, name = cats()