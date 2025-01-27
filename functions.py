def greetCustomer():
    print("Hey,Welcome to Capgemini")
    greetCustomer()

#function with parameters
def greetCustomer(name):
    print("Hey",name,"Welcome to Capgemini")
    greetCustomer("Dheeraj")
    
def sum(a,b):
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    addition=a+b
    add=sum(a,b)
    print(f'The sum of {a} and {b} is {add}')
    
    
def getEmployeeInfo(name="Dheeraj",designation="Software Engineer"):
    print(f'Name:{name} \n Designation:{designation}')
    getEmployeeInfo()
    getEmployeeInfo("Aravind","Senior Software Engineer")
    
    
def customerInfo(name,age,location='Hyerabad'):
    print(f'Name:{name} \n Age:{age} \n Location:{location}')
    customerInfo("Dheeraj",21)
    customerInfo("Aravind",21,"Bangalore")