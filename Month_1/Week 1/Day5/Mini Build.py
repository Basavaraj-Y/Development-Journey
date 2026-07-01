#Simple "Student Management CLI" : Store name + marks in dictionary
students = {}
n = int(input("Enter number of students:"))

for i in range(n):
    name = input(f"Enter Student Name:")
    marks = int(input("Enter marks:"))
    students[name] = marks

print("\nStudent records")

for name, marks in students.items():
    print(name, ":", marks)


#search student in dictionary
search_student = input("Enter name to search:")

if search_student in students:
    print("marks :", students[search_student])
else:
    print("Student not found")


