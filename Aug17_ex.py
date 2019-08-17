
dict= {0: 'chloe', 1: 'Maddy', 2: 'Nanwen', 3: 'Marc'}

dict
print(dict)

a_list_tuples = [
    ('chloe', 'description', 'wears glasses'),
    ('maddy', 'position', 'is sitting'),
    ('cass', 'location', 'is online'),
    ('marc', 'activity', 'is mentoring')
]

a_list_tuples2 = [
    ('chloe', 'wears glasses'),
    ('maddy', 'is sitting'),
    ('cass', 'is online'),
    ('marc', 'is mentoring')
]

# This is our sample data
data = [("Milter", "Miller", 4), ("Milter", "Miler", 4), ("Milter", "Malter", 2)]

# dictionary we want for the result
dict2 = {}

for name, desc, status in a_list_tuples:
    dict2.setdefault(name, {})[desc] = status

print(dict2)

dict3= {}

for name, status in a_list_tuples2:
    dict3.setdefault(name, status)

print(dict3)