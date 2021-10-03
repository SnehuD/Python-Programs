k = 5
for i in range(0, k):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(k, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print()
