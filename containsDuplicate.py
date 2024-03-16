
def containsDuplicateWithSet(*listOfElements):
    # create an empty set
    elements_set = set()

    # Iterating each element and adding it to the set
    for element in listOfElements:
        elements_set.add(element)

    if len(listOfElements) != len(elements_set):
        return True    
    
    return False
    
print("Contains Duplicate? ", containsDuplicateWithSet(*[1, 2, 3]))
print("Contains Duplicate? ", containsDuplicateWithSet(*[1, 2, 3, 1]))