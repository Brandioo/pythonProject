my_list = [5, 4, 3, 2, 5, 1]
n = len(my_list)

for i in range(n):
    for j in range(0, n - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j+1]=my_list[j+1],my_list[j]
print(my_list)