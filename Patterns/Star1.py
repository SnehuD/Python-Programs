print("1st method")
k = 5
for i in range(0, k):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

print()
print("2nd method")
k = 5
for j in range(1, k + 1):
    print("*" * j)