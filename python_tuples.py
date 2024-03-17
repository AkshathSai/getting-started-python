# Tuples are used for high performing SOLID code
# The one difference between Tuples and Lists is that tuple values are immutable
# i.e. values cannot be changed

# my_Tuple = (1, 'strings', 4.5, True)
# or
my_Tuple = 1, 'strings', 4.5, True

print(my_Tuple[1]) # index based access

print(my_Tuple.count('strings')) # gives back the index of where the value is in Tuple


# To iterate over the values in Tuple
for x in my_Tuple:
    print(x)

# my_Tuple[0] = 5 # gives error
