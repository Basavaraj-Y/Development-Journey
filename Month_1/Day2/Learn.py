#if statement
a = 10
b = 20

if b>a:
    print("b is greater than a")

#short hand if statement
if b > a: print("b is greater than a")

#using variables in if statement
is_raining = True
if is_raining:
    print("Don't forget to take an umbrella!")


#elif statement
age = 22

if age < 10:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 30 :
    print("You are an adult.")


#else statement
x = 10
y = 15

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

#short hand if else statement
raining = True
not_raining = False

print("Its raining") if raining else print("Its not raining")


#logical operators
#and operator
j = 5
k = 10
l = 15

if j < k and k < l:
    print("Both conditions are true")

#or operator
if j < k or k < l:
    print("At least one condition is true")

#not operator
if not j > k:
    print("j is not greater than k")


#nested if statement (when if statement is inside another if statement called nested if statement)
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


#pass statement (when we want to write an if statement but we don't want to write any code inside it, we can use pass statement)
age = 30

if age>=18:
    pass
else:
    print("You are too young to drive")

#comparison operators
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True  
