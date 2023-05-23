import csv

with open('../labels.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    breeds = {}
    total_examples = 0

    for row in reader:
        total_examples += 1
        breed = row['breed']

        if breed in breeds:
            breeds[breed] += 1
        else:
            breeds[breed] = 1

print("All breeds: ", len(breeds))
print("Examples:")
i = 0
for breed, count in breeds.items():
    i += 1
    print(f'{1}.{breed}')
print("Total: ", total_examples)
