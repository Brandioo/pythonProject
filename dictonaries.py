my_dict = {
    "brand": "Benz",
    "model": "ML",
    "year": 2008
}

# Dictonary
print("-----------------------")
my_key = None
for cel, val in my_dict.items():
    print(cel, val)
    if val == "Benz":
        print(my_key == cel)
        print("Key Found", cel)
# my_dict.pop(cel)
print(my_dict)
