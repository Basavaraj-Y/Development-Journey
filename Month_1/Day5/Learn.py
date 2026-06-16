#List and Dictionaries
#Lists
'''
my_list = ["Basu", "Lakki", "Poorvi", "Nihal"]
print(my_list)

#list items of any data types
datatype_list = [1, "hello", 20.10, True]
print(type(datatype_list))

#Allow duplicates
new_list = ["apple", "banana", "apple", "orange"]
print(new_list)

#access items
print(new_list[3])   #the first item has index 0

#Range of indexes
print(my_list[1:3])    #the search wil start at 1 and end at 3(not included)
print(my_list[:4])
print(my_list[1:])

#check if item is exists
if "banana" in new_list:
    print("yes, banana is exist in new_list")

#change list items
this_list = ["apple", "kiwi", "orange", "banana"]
print(this_list)
this_list[1] = "cherry"
print(this_list)

#change the range of item values
this_list[1:2] = ["mango", "waterlemon"]
print(this_list)

#insert value without replacing
this_list.insert(2,"kiwi")      #insert an item at specified index
print(this_list)

#add list items
this_list.append("cherry")      #add items at the end of the list

#extend list
this_list.extend(my_list)
print(this_list)

#remove list items
#remove specific items
this_list.remove("banana")
print(this_list)

#remove specific index
this_list.pop(2)
print(this_list)

#del keyword can be used for deleting items at specified index and also delete list completely
del this_list[0]
print(this_list)

#clear() keyword can be used for clear list.in that list will be there but items are all deleted


#loop through a list
for x in this_list:
    print(x)

for i in range(len(this_list)):
    print(this_list[i])

#List comphrension
newlist = [x for x in my_list if "B" in x]
print(newlist)

#sort list
my_list.sort()    #sort values in ascending,alphanumerically
print(my_list)

'''


#Dictionary

thisdict = {
    "name" : "Basu Y T",
    "Age"  : 22,    
    "Role" : "dev learner",
    "Age"  : 23              #duplicates are not allowed
}

print(thisdict)
print(thisdict["name"])

x = thisdict.values()
print(x)

y = thisdict.items()
print(y)

#change values
thisdict["Role"] = "SDE learner"
print(thisdict)

#adding items
thisdict["Habits"] = ["Book reading", "Watch Movies", "Running"]
print(thisdict)

#remove items
thisdict.pop("Habits")
print(thisdict)


#Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Basu",
    "year" : 2004
  },
  "child2" : {
    "name" : "Poorvi",
    "year" : 2005
  },
  "child3" : {
    "name" : "Akira",
    "year" : 2006
  }
}

print(myfamily["child2"]["name"])