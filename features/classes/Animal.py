class Animal:
    NAME = ""
    AGE = 0

    # constructor
    def __init__(self, name, age):
        self.NAME = name
        self.AGE = age

    def print_details(self):
        print(f"Name: {self.NAME}, age: {self.AGE}.")


my_dog = Animal("Pupi",21)
my_dog2 = Animal("Shiro",21)
my_dog.print_details()

print(my_dog.NAME, ",", my_dog2.NAME)
