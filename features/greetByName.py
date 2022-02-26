# Function definition of greet_by_name (name)
def greet_by_name(name):
    print(f"Hello, {name}")

# Call function greet_by_name (name) with "John" as the name argument
greet_by_name("John")

# Function for printing the name and surname
def print_full_name(name, surname):
    print(f"{name} {surname}")
# Calling a function without specifying thr parameter names
print_full_name("Jon", "Snow")
# Function call with names of all parameters
print_full_name(name="Jon", surname="Snow")
# Calling the function with the names of the last parameter
print_full_name("Jon", surname="Snow")

def print_hello(text: str) -> None:
    print(f"Hello {text}")

print_hello("world")

# The definition of the function greet_by_name (name) with the default value of the name
def greet_by_name(name="World!"):
    print(f"Hello, {name}")
# # Calling the function greet_by_name (name) without an argument
greet_by_name()  # Prints "Hello, World!"
# # Calling the function greet_by_name (name) with "John" as the name argument
greet_by_name("John")  # Prints 'Hello, John'
greet_by_name(name="John")  # Prints 'Hello, John'

def get_hello(text: str) -> str:
    return f"Hello {text}"


print(get_hello("world"))