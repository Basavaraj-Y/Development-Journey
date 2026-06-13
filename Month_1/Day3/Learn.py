#For loop

fruits = ["apple", "banana", "mango", "grape"]

for x in fruits:
    print(x)

#break statement
    if x == 'mango':
        break
    print(x)

    if x == 'banana':
        print(x)
        break 

#continue statement
for x in fruits:
    if x == 'banana':
        continue
    print(x) 

#else statement in for loop
for x in fruits:
    print(x)
else:    print("No more fruits to print")


#range function
for x in range(13):
    print(x) 

#while loop
i = 1

if i < 8:
    print(i)

while i < 8:
    print(i)
    if i == 3:
        break
    i += 1

while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)

#else statement in while loop
while i < 8:
    print(i)
    i += 1
else:
    print("i is no longer less than 8")
