
simple_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(simple_dict[1]) # accessing a value using it's key

simple_dict[2] = 'Mint Tea' # update a value using it's key
print(simple_dict)

del simple_dict[3] # Delete based on the key
print(simple_dict)

my_dic = {1: 'Test', 'Name': 'Jim'}
print(my_dic)

my_dic[2] = 'Test 2'
print(my_dic)

my_dic[1] = 'Not a Test!'
print(my_dic)

# Iterating through a dictionary
for x in my_dic:
    print(x)

for key, value in my_dic.items():
    print(str(key) + " : " + value)

