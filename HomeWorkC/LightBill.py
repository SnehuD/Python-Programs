cno = input('Enter customer number\t : ')
cname = input('Enter customer name\t : ')
nou = int(input('Enter number of units\t : '))

t1 = 0
t2 = 0
t3 = 0
ft = 0

if nou < 100:
    t1 = nou * 3.33

elif 101 <= nou < 200:
    t1 = 100 * 3.33
    t2 = 200 * 7.33

elif nou >= 301:
    t1 = 100 * 3.33
    t2 = 200 * 7.33
    t3 = (nou - 300) * 11.33

ft = t1 + t2 + t3;

print('\n----------------------------------Your Billing Details----------------------------------')
print('Customer Number\t : ', cno)
print('Customer Name\t : ', cname)
print('Number of Units\t : ', nou)
print('Total Bill\t : ', ft)
