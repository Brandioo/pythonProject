import time
from time import sleep
import time

start_time = time.time()

ages = [25, 26, 4, 89, 29, 19]

max_age = 1
for age in ages:
    print(f"{age} > {max_age}")
    if age > max_age:
        max_age = age
    sleep(2)

print(max_age)

print("--- %s seconds ---" % (time.time() - start_time))
