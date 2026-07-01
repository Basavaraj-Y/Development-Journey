
#Print multiplication table
num = int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Sum of numbers 1–100
total = 0

for i in range(1,101):
    total += i
print("sum : ",total)

#Reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number:", reverse)

#Count vowels in string
text = input("Enter a text:")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1
print("Nmber of Vowels : ",count)