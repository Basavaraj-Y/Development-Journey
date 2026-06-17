#Remove duplicates 
'''
numbers = [1, 1, 2, 3, 4, 3, 5, 4, 6]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Atfer Removing Duplicates:", unique_numbers)


#Word Frequency counter
sentence = input("Enter a sentence:")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies")

for word, count in frequency.items():
    print(word , ':', count)
'''
#Student Marks Dictionary
student_dict = {
    "student1" : {
        "name" : "Basu",
        "marks" : 80
    },
    "student2" : {
        "name" : "Lakki",
        "marks" : 90
    },
    "student3" : {
        "name" : "Poorvi",
        "marks" : 85
    }
}

for i in student_dict.values():
    print(i["name"], ":", i["marks"])

