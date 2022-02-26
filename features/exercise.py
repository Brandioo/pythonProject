# Add any number of numbers
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(add(1, 2, 3, 4, 5))  # Prints 15


# Prints the name and what the user gives
def print_name_and_something(name, *strings):
    print(f"First name: {name}")
    for string in strings:
        print(string)

# Add any number of ingredients
def add_ingredients(**kwargs):
    result = 0
    for key in kwargs:
         result += kwargs[key]
    return result

print(add_ingredients(eggs=3, spam=5, cheese=2))  # Will print 10


# Add any number of ingredients
def add_ingredients(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        result += kwargs[key]
    return result


print(add_ingredients(1, 2, 3, eggs=3, spam=5, cheese=2))  # Will print 16
