k = 65
for i in range(0, 7):
    for j in range(0, i + 1):
        ch = chr(k)
        print(ch, end=" ")
        k += 1
    print()
