x = int(input("Enter: "))

if x % 3 == 0 and x % 5 == 0:
    print("Fizz Buzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0:
    print("Fizz")
else:
    print(f"Number does not have any subdivision with 5 or 4. Nr = {x}")
