accno = int(input('Enter Account Number\t\t : '))
name = input('Enter your Name\t\t\t\t : ')
mbal = float(input('Enter Monthly Balance\t\t : '))
mfd = int(input('Enter no. of Months for FD\t : '))

total = mbal * mfd
i = total * 0.08
fbal = total + i

print('\n-------------------------Account Details------------------------')
print('Account Number\t : ', accno)
print('Your Name\t\t : ', name)
print('Monthly Balance\t : ', mbal)
print('No. of Months\t : ', mfd)

print('Total Amount\t : ', total)
print('Interest\t\t : ', i)
print('Final Balance\t : ', fbal)
