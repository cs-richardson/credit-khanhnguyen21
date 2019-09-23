creditNum = int(input('Credit Card Number:'))
cred = creditNum
total = 0
i = len(str(cred))
if i == 15 or i == 13:
    for x in range (i):
        number = int(cred % 10)
        cred = int(cred/10)
        if x % 2 == 0:
            total = total + number
        else:
            number = number * 2
            total = total + int(number % 10) + number // 10
    if total % 10 == 0:
        if i == 13:
            print('Visa')
        else:
            print('AmEx')
    else:
        print('Invalid')
elif i == 16:
    for x in range (i):
        number = int(cred % 10)
        cred = int(cred/10)
        if x % 2 != 0:
            number = number * 2
            total = total + int(number % 10) + number // 10
        else:
            total = total + number
    if total % 10 == 0:
            if int(creditNum / 1000000000000000) == 4:
                print('Visa')
            else:
                print('MasterCard')
    else:
        print('Invalid')
else:
    print('Invalid')
        
