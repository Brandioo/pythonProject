car = {
    "brand": "Mercedes",
    "model": "ML",
    "year": 1964,
    "type": ["Foristrad", "Veture"]
}

print(car.values())

# car.popitem()
# car.pop("model")
# print(car)

for x in car:
    print(x, car[x])
