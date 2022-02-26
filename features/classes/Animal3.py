class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter - delete the field
    def age(self):
        del self.__age


my_dog = Animal('Gog', 12)
del my_dog.age

my_dog = Animal('Dog', 11)
my_dog.age = 3  # Sets age - uses setter
print(my_dog.age)  # Reads age - uses a getter