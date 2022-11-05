import time

A = input("number of presicenesss (must be even):")
print(A)

i = int(0)
b = float(0)
x = int(0)
y = int(2)

start_time = time.time()

while i < int(A):
    b += (4/(1+x))-(4/(1+y))
    i += 2
    x += 4
    y += 4
else:
    print("Pi =")
    print(b)

print("--- %s seconds ---" % (time.time() - start_time))
