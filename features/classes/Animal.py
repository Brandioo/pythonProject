class Animal:
    NAME = ""
    AGE = 0

    # constructor
    def __init__(self, name, age):
        self.NAME = name
        self.AGE = age

    def print_details(self):
        print(f"Name: {self.NAME}, age: {self.AGE}.")


my_dog = Animal("ok",21)
my_dog.print_details()

print(my_dog.NAME)
