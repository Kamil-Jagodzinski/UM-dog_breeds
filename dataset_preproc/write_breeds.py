import csv
from collections import OrderedDict

breed_dict = OrderedDict()

with open('../labels.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        _, breed = row
        breed_dict.setdefault(breed, None)

breed_list = list(breed_dict.keys())

i = 0 
for breed in breed_list:
    print(f'"{i}.{breed}",')
    i += 1