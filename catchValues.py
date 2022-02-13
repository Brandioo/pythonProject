thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", {"white": 101, "dd": 102}, "blue"]
}

# n = thisdict["colors"]
# print(n)
# m = n[1]
# print(m)
# l = m["white"]
# print(l)
x = thisdict.keys()
for key in x:
    print(key)
# print(x)

if "brand" in thisdict.keys():
    print("Yes")