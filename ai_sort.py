# GitHub Copilot suggestion
def sort_dicts_ai(data_list, key):
    return sorted(data_list, key=lambda d: d[key])

# Sample data
people = [
    {'name': 'Alice', 'age': 34},
    {'name': 'Bob', 'age': 23},
    {'name': 'Charlie', 'age': 29}
]

# Sorting by 'age'
sorted_people_ai = sort_dicts_ai(people, 'age')
print("AI:", sorted_people_ai)

