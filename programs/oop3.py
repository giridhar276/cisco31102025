


#class - create our own implementation
class Employee:
    def getName(self,name):
        self.name = name
    def displayName(self):
        print("Name:", self.name)

# object creation
emp1 = Employee()
emp1.getName("rita")
emp1.displayName()

#########
emp2 = Employee()
emp2.getName("gita")
emp2.displayName()