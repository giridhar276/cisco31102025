customers = {
      "C001": {"name": "Alice", "balance": 5000},
      "C002": {"name": "Bob", "balance": 12000},
      "C003": {"name": "Charlie", "balance": 3000}
  }


for key,value in customers.items():
    customers[key]['balance']+=1000

print(customers)