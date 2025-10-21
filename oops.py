'''class cars:
    model="mazda"
    color="cherry red"
cars1=cars()
print(cars1.model)
print(cars1.color) 


class car:
    def __init__(self,company,model):
        self.company= company
        self.model= model

s1=car("veda","ferrari")
print(s1.company,s1.model) 


class cars:
    def __init__(self,modelname,company):
        self.modelname= modelname
        self.company=company
    def display(self):
        print(f"{self.modelname} is {self.company}")

vedang=cars("v","f")
print(vedang.modelname,vedang.company)
vedang.display()





class application:
    def __init__(self):
        self.a=int(input("Enter the value"))
        self.b=int(input("enter the value of b"))
    def calculate(self):
        self.c=self.a*self.b
        print(self.c)
        
goat=application()
goat.calculate()
            



class user:

    name="not found"
    def __init__(self,name,car):
        self.name=name
        self.car=car


cars=user("vedang","lamborghini")
print(cars.name,cars.car)

'''


class student:
    def __init__ (self,name,subject1,subject2,subject3):
        self.name=name
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
    def average(self):
        self.avg=(self.subject1+self.subject2+self.subject3)/3
    def display(self):
        print(f"{self.name}",self.avg)

practice=student("vedang",22,23,27)
practice.average()
practice.display()