while 'true':
    print('1).Factor')
    print('2).Factorial')
    print('3).Prime')
    print('4).Reverse')
    print('5).Sum Of Digit')

ch: int=int(input('Enter Your Choice : '))
if ch==1:
    print('Factors')

elif ch==2:
    print('Factorials')

elif ch==3:
    print('Prime')

elif ch==4:
    print('Reverse')

elif ch==5:
    print('Sum of Digit')

else:
    print('Wrong Choice..')

print('Do You Want to Continue??\nPress 1 : ')
    ch=input()
    if ch!=1:
        break;
    print('Test')
print('Thank You!!')