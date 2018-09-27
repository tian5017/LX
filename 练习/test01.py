

for x in range(1, 10):
    y = 20 - 2 * x
    z = 30 - x - y
    if 3 * x + 2 * y + z == 50:
        print(x, y, z)


n = 7
while not ((n % 2 == 1) and (n % 3 == 2) and (n % 5 == 4) and (n % 6 == 5) and (n % 7 == 0)):
    n = n + 7
print(n)