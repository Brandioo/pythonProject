# print("What", "a", "beautiful", "day", ".", sep="-")
# print("-" * 45)
# print("What", "a", "beautiful", "day", ".", sep="\n")
# print("-" * 45)
# print("What", "a", "beautiful", "day", ".", sep="\t")
# print("-" * 45)
# print("What", "a", "beautiful", "day", ".", sep="\n", end="! \n")
# print("-" * 45)
# print("1", "2", 3, 4, 5,sep=",")
# print("-" * 45)
# fruit = "orange"
# print(fruit)

# print("-" * 45)

# title="General"
# name="Kenobi"
# age=28
# print("Hello, %s %s ", (title,name   ))
# print("Hello there, {} {}".format(title, name))
# print("Hello there", {title}, {name}, {age})
# print(f"Hello there {title}, {name}, {age}")

# print("-" * 45)

header1="Name"
header2="Age"
name = "John"
age=22
print(f"| {header1} | {header2} |")
print(f"| {name} | {age} |")

print("-" * 45)

n=109.234555
print(f"{n: .3f}")

percent = 0.71
print(f"{percent: .3%}")

ok1="12345"
print(ok1.isprintable())

ok2="Hello\tWorld"
print(ok2.isprintable())

ok3="HelloWorld\n"
print(ok3.isprintable())

greet1="Hello World"
print(greet1.istitle())

greet2="Hello WORLD"
print(greet2.istitle())

greet3="Is It Good"
print(greet3.istitle())

str1=","
str2="Hello"
print(str1.join(str2))

# str3="-->"
# str4="Hello"
# print(str3.join(str4))

# space="      Hello World     "
# space.lstrip()
# space.rstrip()
# print(space.strip())

# Hide - symbol in right and in left
# space="-------Hello World-------"
# space.lstrip()
# space.rstrip()
# print(space.strip("-"))

# string1="Hello World"
# print(string1.partition())

replacement="Hello World"
print(replacement.replace("Hello","Hi"))

rfind1="Hello World"
print("Index of o: ",rfind1.rfind("o"))

split1="HelloWorld"
print("Split",split1.split("W"))

