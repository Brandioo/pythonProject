my_list = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    {
        "brand": "Audi",
        "model": "Q7",
        "year": 2008
    },
    {
        "brand": "BMW",
        "model": "X7",
        "year": 2022
    }
]

is_available = False

for my_dictionary in my_list:
    a = my_dictionary["model"]
    if a == 'Q7':
        is_available = True

if is_available:
    print("Yes")
else:
    print("No")
