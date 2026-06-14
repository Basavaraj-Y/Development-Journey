#Functions 
#def function
def my_functions():
    print("Hello from a Functions.")

my_functions()

#return value
def new_function():
    return "Hello from a return value"

message = new_function()
print(message)

#Parameters and Arguments
def names(name):      #name is a parameter
    print("Hello", name)

names("basu")         #basu is a argument
names("lakki")        #lakki is a argument

#number of arguments
def f_l_names(fName,lName):
    print(fName + ' ' + lName)

f_l_names("Basu", "Y T")
#Keyword arguments
f_l_names(fName="lakki", lName="Y T")

#Default parameter values
def my_course(course = "AI & DS"):
    print("Hello", course)

my_course()
my_course("CSE")
my_course("ECE")

#Scope
#local Scope
def values():
    x = 10
    print(x)
values()

#Global Scope
a = 100

def my_value():
    print(a)

my_value()

#lambda Function
x = lambda a, b : a * b

print(x(2,3))

def lambda_example(y):
    return lambda x: x + y

add1 = lambda_example(5)
add2 = lambda_example(8)

print(add1(5))
print(add2(12))
