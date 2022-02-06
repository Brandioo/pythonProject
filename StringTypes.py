# a="hello world"
# b=a.capitalize()
# print(b)
# print(a.upper())
# print("-----------------------")
# greet = 'Test'
# print(greet.center(5,'-'))
# print(greet.center(6,'='))
# print(greet.center(7,'>'))
# print(greet.center(22,' '))
# print(len(greet))

# mystr="Training is a free online Train 4 Trainers"
# substr="Tutorials"
#
# total=mystr.count("Train")
# print("Number Of occurrences of 'Train': ", total)
#
# total=mystr.count(substr,0,15)
# print("Number of occurrences between 0 an 15 index: ", total)
#
# total=mystr.count(substr,10,44)
# print("Number of occurrences between 15 an 25 index: ", total)

# mystr="Hello World"
# substr="l"
# total=mystr.count(substr)
# print(total)

# greet = "Hello World"
# print("Index of H: ", greet.index('H'))
# print("Index of e: ", greet.index('e'))
# print("Index of l: ", greet.index('l'))
# print("Index of World: ", greet.index("World"))

greet = "bob@gmail.com"

print('Index of @:', greet.index('@'))
at_idx = greet.index('@')
if at_idx < 3:
    print("Not Valid")
else:
    print("Valid")
