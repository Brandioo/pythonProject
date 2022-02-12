my_str = input("Jep Str: ")
upper_cnt = 0
lower_cnt = 0

for chr in my_str:
    if chr.isalpha():
        if (chr.isupper()):
            upper_cnt += 1
        else:
            lower_cnt += 1

print(f"Upper CASE = {upper_cnt}")
print(f"Lower CASE = {lower_cnt}")
