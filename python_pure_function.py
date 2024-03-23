myList = [1,2,3]

# Pure functions do not alter global scope data

def addItemToList(list, item):
    newList = list.copy()
    newList.append(item)
    return newList

print(myList)
print(addItemToList(myList, 4))
print(myList)