my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_s = 0

for val in my_list:
    if val == 7:
        print("Found!")
        break
    # print(val)
print("Here")

# for val in my_list:
#     if val == 10:
#         continue
#     my_s += val
# print(my_s)

n = 0
while n < 5:
    n += 1
    if n == 4:
        pass
        # break
    # print("Er")
    if n == 1:
        continue
    print(n)
