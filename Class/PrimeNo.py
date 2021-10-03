print('1st Method')
num = 3
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'is not a Prime Number!!')
            print(i, 'Times', num // i, 'is', num)
            break
        else:
            print(num, 'is a Prime Number!!')
    else:
        print(num, 'is not a Prime Number!!')

print('\n\n')
print('2nd Method')
start = 11
end = 25
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                print(i)