#Error handlling and file handling

#Exception Handling
#try/except
try:
  print(x)
except:
  print("An exception occurred")

#Many Exceptions
try:
  print(y)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Raise an exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


#Reading/writing files
f = open("demofile.txt")
print(f.read())
f.close()

#with statement
with open("demofile.txt") as f:
    print(f.read(5))
    print(f.readline())       #read first line in file

#write to an existing file
#"a" - Append : will append to the end of the file
#"w" - Write : will overwrite any existing content

#appending the content to file
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content.")

f = open("demofile.txt")
print(f.read()) 

#overwrite existing content
with open("demofile.txt", "w") as f:
  f.write("Woops, I have deleted the content.")

with open("demofile.txt") as f:
  print(f.read())


#JSON basics
import json     #import the JSON module

#Parse JSON : convert from JSON to Python
#JSON
x = '{"name" : "Basu", "age" : 22, "city" : "Bengaluru" }'

#parse
y = json.loads(x)

#the result is a Python dictionary
print(y["age"])


#Convert from Python to JSON
import json

#Python dictionary(object)
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#convert into JSON
y = json.dumps(x)

#the result is a JSON string
print(y)

'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''

import json

print(json.dumps({"name": "Lakki", "age": 40}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))