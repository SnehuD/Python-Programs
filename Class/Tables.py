# Print 1 to 10 tables
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, '\t', end=" ")
        j += 1
    i += 1
    print()
