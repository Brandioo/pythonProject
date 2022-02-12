speed = int(input("Speed: "))
license_point = int(input("Patent Points: "))
limit = 5
speedlimit = 70
speedmin = 20

if speedmin <= speed <= speedlimit:
    print("Ok")
elif speed <= speedmin:
    print("Be Careful")
else:
    speed_diff = speed - speedlimit
    point = speed_diff // limit
    if (point <= license_point):
        print("Points: ", point)
        print("License Point left: ", license_point - point)
    else:
        print("License Suspended")
