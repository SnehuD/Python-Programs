# Program to convert Pressure in kilopascals to pounds per square inch
# a milimeter to mercury (mmHg) & atmosphere Pressure

kpa = float(input('Enter Pressure in KiloPascal\t\t\t : '))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325

'''
print('The Pressure in Pounds per Square inch : %.2f psi' % (psi))
print('The Pressure in Milimeter of Mercury : %.2f mmHg' % (mmhg))
print('Atmosphere Pressure : %.2f atm.' % (atm))
'''

print('The Pressure in Pounds per Square inch\t : ',psi)
print('The Pressure in Milimeter of Mercury\t : ',mmhg)
print('Atmosphere Pressure\t\t\t\t\t\t : ',atm)
