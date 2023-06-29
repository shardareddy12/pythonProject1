class Vehicle:
    car_list=[]
    car= "audi"
    def __init__(self,max_speed, mileage):
        self.max_speed= max_speed
        self.mileage= mileage

obj= Vehicle(100,20)
obj.car_list.append("mazda")
print("max_speed",obj.max_speed)
print(obj.car_list)
print("mileage",obj.mileage)


#####################################################################



class Player:
    teamName = 'Liverpool'      # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name        # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)


p1 = Player('Mark')


print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
p2 = Player('Steve')
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)




################################################################################

class Employee:

    update_salary = 10
    depart_name = "HR"

    def __init__(self,ID=None, Salary=None,department=None):
        self.ID= ID
        self.Salary=Salary
        self.department= department

    def tax(self):
        return(self.Salary*0.2)

    def salaryPerDay(self):
        return(self.Salary /30)

    def demo(self,a,b=3,c=None):
        print("a=",a)
        print("b=",b)
        print("c=",c)
    @classmethod
    def demo1_cls(cls, new_dep_name):
        cls.depart_name = new_dep_name
        print(new_dep_name)

steve = Employee(32,2500,"HR")
'''

print(steve.ID)
print(steve.Salary)
print(steve.tax())
print(steve.salaryPerDay())
'''

print("demo")
print(steve.demo(1,2))
print(steve.demo(3,2,2))

Employee.demo1_cls("tech")


