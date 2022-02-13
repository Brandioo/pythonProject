fruits = ["Apple", "Banana", "Lemon","qe","qu"]

for index, fruit in enumerate(fruits):
    print(f"Fruits: {fruit}, under the index: {index}")
    if index % 2 == 0:
        fruits.pop(index)
print(fruits)