# Function to sort a list of dictionaries manually by a given key
def sort_dicts_manual(data_list, sort_key):
    return sorted(data_list, key=lambda x: x[sort_key])

# Sample data
people = [
    {'name': 'Alice', 'age': 34},
    {'name': 'Bob', 'age': 23},
    {'name': 'Charlie', 'age': 29}
]

# Sorting by 'age'
sorted_people_manual = sort_dicts_manual(people, 'age')
print("Manual:", sorted_people_manual)

