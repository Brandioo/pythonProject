# Fibonacci
# 0,1,1,2,3,5,8,13...

nr = int(input("Enter Fibonacci Nr: "))
p2 = 0
p1 = 1
print(p2)
print(p1)

for i in range(0, nr - 2):
    cn = p1 + p2
    print(cn)
    p2 = p1
    p1 = cn
