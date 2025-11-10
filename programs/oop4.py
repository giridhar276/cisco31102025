


#class - create our own implementation
# constructor : begins with __init__ 
class Employee:
    def __init__(self,name):
        self.name = name
    def displayName(self):
        print("Name:", self.name)

# object creation
emp1 = Employee("rita")
emp1.displayName()

#########
emp2 = Employee("sita")
emp2.displayName()