# list of dictionaries
products = [
      {"id": 101, "name": "Laptop", "price": 75000},
      {"id": 102, "name": "Mobile", "price": 25000},
      {"id": 103, "name": "Tablet", "price": 15000}
  ]


print(type(products))
print(isinstance(products,list))  # True
print(isinstance(products,dict))  # False

for product in products:
    if 'name' in product and 'price' in product:
        print(product['name'] , product['price'])
