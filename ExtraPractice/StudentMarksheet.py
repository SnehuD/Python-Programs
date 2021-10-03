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
print('------------------------THANK YOU-------------------------------------')

print('\n\n\n\n---------------------------------------------------------------------------')
print('RollNo\tStudent Name\tSub1\tSub2\tSub3\tTotal\tPercentage')
print('\n---------------------------------------------------------------------------')
print(rn, '\t', sn, '\t', s1, '\t', s2, '\t', s3, '\t', total, '\t', prcnt)
print('\n---------------------------------------------------------------------------')
