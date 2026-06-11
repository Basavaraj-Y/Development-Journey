#Syntax of Python
print("Hello World!")

#python indintation
if 10 > 5:
    print("10 is greater than 5")

#print text and numbers
print("Hello Pytrhon")
print(10)

#print txt and numbers together
print("my age is", 22)


#Variables in Python
#creating variables
x=3
y="Basu Y T"
z=20.04


#casting
a=str(x)         # casting int to str
b=float(y)       # this will give an error because y is not a number
c=int(z)         # casting float to int (no change)


#Get the type
print(type(x))      # this will print <class 'int'>
print(type(y))      # this will print <class 'str'>
print(type(z))      # this will print <class 'float'>


#single and double quotes
name1 = 'Lakki'
name2 = "Love"


#case sensitive
Name="Lakki"
#is not the same as
name="Lakki"


#Variable names
#Variable names can contain letters, numbers, and underscores, but they cannot start with a number. They are also case sensitive.

my_variable = "This is a variable"
myVariable = "This is also a variable"
_my_variable = "This is also a variable"
myVariable2 = "This is also a variable"

#but 2myVariable  = "This will give an error because variable names cannot start with a number"


#variable names
#1camel case : each word , except first word starts with capital letters
myVariableName = 'This is Camel Case'

#2Pascal case : each word starts with capital letters 
MyVariableNAme = 'This is a pascal case'

#3snake case : each word is separated by an underscore
my_variable_name = 'This is a snake case'


#many values to multiple variables
x, y, z = "green", "blue", "red"
print(x)      # this will print "green"
print(y)      # this will print "blue"  
print(z)      # this will print "red"  

#one value to multiple variables
x = y = z = "Basu Y T"
print(x)      # this will print "Basu Y T"
print(y)      # this will print "Basu Y T"
print(z)      # this will print "Basu Y T"

#output variables
x = "Python is best"
print(x)     # this will print "Python is best"

#global variables
x = "python"

def myfunc():
    print(x)

myfunc()     # this will print "python"

#global keyword
def myfunc():
    global x      # this will make x a global variable inside the function using global keyword
    x = "python is best"    

myfunc()
print(x)     # this will print "python is best" 



#input/print
name = input("Enter your name: ")     # this will prompt the user to enter their
print(name)

