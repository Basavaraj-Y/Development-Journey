#largest of three numbers
a = int(input("Enter first number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter third number:"))

if a>=b and a>=c:
    print("A is the largest number")
elif b>=a and b>=c:
    print("B is the largest number")
else:
    print("C is the largest number")


#Grade calculator 
marks = float(input("Enter your marks:"))

if marks>90:
    print("First class")
elif marks>70:
    print("Second class")
elif marks>50:
    print("Third class")
elif marks>35:
    print("Pass")
else:
    print("Fail")


#leaf year checker
year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leaf year")
else:
    print(f"{year} is not a leaf year")

