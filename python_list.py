
list1 = [1, 2, 3, 4, 5]
print(list1[2]) # Accessing an element 3 from the list

list2 = ['A', 'B', 'C']
print(*list2) # to print the entire list

list3 = ["Hello", 123, 3000, True]

print(*list3)
print(list3, sep=" ") # shows how the list looks like in the code

# To add an element to a list
list1.insert(len(list1), 6) # Index based insertion
print(*list1)

list1.append(7) # Appends an element at the end of the list
print(*list1)

list1.extend([8, 9 , 10]) # To add multiple elements to the list
print(*list1)

# To remove an element from the list
list1.pop(4) # index based removal
print(*list1)

del list1[2] # index based removal
print(*list1)

# Iterate through a list
for x in list1:
    print("Value ", x)
  