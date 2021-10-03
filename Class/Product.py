pid = input('Enter Product ID\t : ')
pn = input('Enter Product Name\t : ')
pp = float(input('Enter Product Price\t : '))
pq = int(input('Enter Product Quantity\t : '))

total = pp * pq
cgst = total * 0.06
sgst = total * 0.06
ft = total + cgst + sgst

print('\n--------------------------PRODUCT INFORMATION----------------------------')
print('Product Id\t\t : ', pid)
print('Product Name\t\t : ', pn)
print('Product Quantity\t : ', pq)
print('Total Price\t\t : ', total)
print('Product Price\t\t : ', pp)
print('CGST\t\t\t : ', cgst)
print('SGST\t\t\t : ', sgst)
print('Final Total\t\t : ', ft)
