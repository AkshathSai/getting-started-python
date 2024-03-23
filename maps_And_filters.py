menu = ['espresso','mocha','latte','cappuccino','cortado','americano']

def findCoffee(coffee):
    if coffee[0] == 'c':
        return coffee

# Both map and filter functions are esentially same the only difference is
# Maps take all objects in a list and applies a function
# Filters do the same, but take the results 
# and creates a new List with only True values    

# map(function, list)
map_coffee = map(findCoffee, menu)
print(map_coffee)    
for x in map_coffee:
    print(x)

# filter(function, list)
filter_coffee = filter(findCoffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)    