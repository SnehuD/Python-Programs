rn = input('Enter ur RollNo : ')
sn = input('Enter ur Name : ')
s1 = int(input('Enter marks for Subject1 : '))
s2 = int(input('Enter marks for Subject2 : '))
s3 = int(input('Enter marks for Subject3 : '))

total = s1 + s2 + s3
prcnt = total / 3

print('\n\n------------------------STUDENT MARKSHEET---------------------------')
print('RollNo\t\t : ', rn)
print('Student Name : ', sn)
print('Math\t\t : ', s1)
print('Comp\t\t : ', s2)
print('Elect\t\t : ', s3)
print('Total\t\t : ', total)
print('Percentage\t : ', prcnt)

if s1 < 40 or s2 < 40 or s3 < 40:
    print('Result\t\t : Fail')
else:
    print('Result\t\t : Pass')
    if 40 <= prcnt <= 60:
        print('Grade\t\t : C')
    elif 60 <= prcnt <= 70:
        print('Grade\t\t : B')
    else:
        print('Grade\t\t : A')

print('------------------------THANK YOU---------------------------')

print('New Method..!!')
print(f'{rn}\t{sn}\t{s1}\t{s2}\t{s3}\t{total}\t{prcnt}')
# f=Formatted String
