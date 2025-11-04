
try:
    with open("employee.csv","r") as emp:
        print(emp.readlines())
except Exception as err:
    print("System Error",err)