id = int(input('Enter the Employee ID\t : '))
en = input('Enter Employee Name\t\t : ')
bs = int(input('Enter the Basic Salary\t : '))

da = bs * 0.25
hra = bs * 0.15
pf = bs * 0.12
ta = bs * 0.075
np = bs + da + hra + ta
gp = np - pf

print('-------------------------Employee Details---------------------------')
print('Employee ID\t\t : ', id)
print('Employee Name\t : ', en)
print('Basic Salary\t : ', bs)

print('Dearness Allow\t : ', da)
print('House Rent Allow : ', hra)
print('Travel Allow\t : ', ta)
print('Net Salary Pay\t : ', np)
print('Provident Fund\t : ', pf)
print('Gross Payment\t : ', gp)
