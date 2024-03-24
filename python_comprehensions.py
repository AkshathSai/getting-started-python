
# list comprehension
# [ <expression> for x in <sequence> if <condition>] 
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+1 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x+1 for x in data]
print("Creating a new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in data if x%4==0]
print("Divisible by 4: ", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
data = [x-1 for x in data if x%4==0]
print("Divisible by four minus one: ", data)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9==0]
print("Nines: ", nines)

# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

# Dictionary comprehension
# Dictionary comprehension takes one or two lists as input and creates a dictionary out of it
# dict = { key:value for key, value in <sequence> if <condition> } 

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numDict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numDict)

# In case of using two lists, the format it follows is: new_dict ={key:value for (key, value) in zip(list1, list2)}
# Using two input lists
months_dict = {key:value for (key, value) in zip(months, number)}
print("Using two lists: ", months_dict)

# Set comprehension
# The set comprehension deals with the set data type and it's very similar to list comprehension. 
# The only key difference is the use of curly brackets for sets instead of square brackets as in lists. 
set_a = {x for x in range(20) if x not in [12, 14, 16]} # not in is a keyword
print(set_a)

# Generator comprehension
# Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
# They are also more memory efficient as compared to list comprehensions.
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")

'''
Here is the difference between map() function and list comprehensions:
newdata = map(square, data)
newdata = [x + 3 for x in data] 

Notice how both map() functions and list comprehension effectively do the same job of modifying iterator sequences such as the list in the example above.

List comprehensions have been a relatively recent development but it does not necessarily mean they are more efficient. 
Comprehensions have gained popularity primarily for providing cleaner code readability and ease of use. 
They also provide some added advantages such as providing filtering using if else conditions.

List comprehensions also provide direct return of a list as compared to map() function that returns a map object.
It is mainly the clarity that has made list comprehensions popular,
but map() functions are still arguably a better choice when it comes to the use of larger sequences.
'''