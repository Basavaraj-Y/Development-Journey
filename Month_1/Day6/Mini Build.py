#Save student data to JSON file.
import json

students = {}

number = int(input("Enter number of students:"))

for i in range(number):
    name = input("Enter student name:")
    marks = int(input("Enter student marks:"))
    students[name] = marks

with open("students.json", "w") as file:
    json.dump(students, file)

print("student data saved successfully.")