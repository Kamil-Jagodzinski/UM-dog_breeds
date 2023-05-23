import csv

def check_unique_ids(file_path):
    id_set = set()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            id = row[0]
            if id in id_set:
                return False 
            id_set.add(id)
    return True  

file_path = '../datset/labels.csv'
are_ids_unique = check_unique_ids(file_path)

if are_ids_unique:
    print("IDs are unique.")
else:
    print("IDs are not unique.")
