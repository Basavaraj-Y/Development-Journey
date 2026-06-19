#Read file & count words
with open("demofile.txt", "r") as file:
    content = file.read()

words = content.split()
print("Total Words:", len(words))



#Handle divide-by-zero safely

try:
    num = int(input("Enter Numerator:"))
    den = int(input("Enter Denaminator:"))

    div = num / den
    print(div)

except ZeroDivisionError:
    print("Error : Cannot divide by zero")

