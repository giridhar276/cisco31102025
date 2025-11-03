employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}

### we are reading the values only
for empdata in employees.values():
    print(empdata['name'] , empdata['department'])

## we are reading key-value pair
for empcode,empdata in employees.items():
    print(empdata['name'] , empdata['department'])