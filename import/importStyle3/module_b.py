# We import only the find_index function

from module_a import find_index

courses = ["PE", "History", "Math"]
index = find_index(courses, "PE")
print(index)  # Prints 0