# Hollow inverted pyramid in Python

n = 5  # number of rows

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i) - 1):
        print(" ", end="")
    if i != n:  # avoid extra stars in the first line
        for j in range(i):
            print("*", end="")
    print()
