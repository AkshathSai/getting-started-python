# Python doesn't have a built-in reverse function
# 2 ways to reverse a String
# 1. Using extended slice function #str[start:stop:step]
# 2. Using slice function along with recursion 

def reverseString(str):
    return str[::-1] # -1 indicates that the String needs to be traversed from the right one index position at a time

print(reverseString('hello'))

def reverseStringRecursive(str):
    if len(str) == 1:
        return str
    else:
        return reverseStringRecursive(str[1:]) + str[0]
    
print(reverseStringRecursive('world'))    