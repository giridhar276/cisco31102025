



#class - create our own implementation

class Employee:
    #constructor - this method is invoked automatically when object is created
    def getName(self,name):
        self.name = name
    def displayName(self):
        print("Emp name :",self.name)

# object creation
emp1 = Employee()
emp1.getName('Ram')
emp1.displayName()


emp2 = Employee()
emp2.getName('Rao')
emp2.displayName()

emp3 = Employee()
emp3.getName('Sita')
emp3.displayName()