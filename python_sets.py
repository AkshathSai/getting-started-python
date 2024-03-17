# Sets are also like Lists but these do not allow duplicate values

set_a = {1, 2, 3, 4, 5, 5}

set_a.add(6) # adds an element 6
print(set_a)

# set_a.remove(2) # removes the element 2
# or
set_a.discard(2) # removes the element 2
print(set_a)

# Mathematical operations using Sets
set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b))
# or
print(set_a | set_b)

print(set_a.intersection(set_b))
# or
print(set_a & set_b)

# difference in sets
print(set_a.difference(set_b)) # gives all the elements present in A but not in B
# or
print(set_a - set_b) 

# Symmetrical difference in sets
print(set_a.symmetric_difference(set_b)) # gives all the elements present in A and B but not in both
# or
print(set_a ^ set_b)

# Set is not sequence hence you can't access elements based on ordered index
# print(set_a[0]) # This gives an error
