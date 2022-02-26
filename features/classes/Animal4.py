class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age


dog_a = Animal()
dog_b = dog_a
print(dog_a.name)  # Display "Rex"
print(dog_b.name)  # Display "Rex"

dog_a.name = "Pongo"
print(dog_a.name)  # Display "Pongo"
print(dog_b.name)  # Display "Pongo"