#Credit
#by Khanh Nguyen

creditNum = int(input('Credit Card Number:'))
#CreditNumber as a disposable varible
cred = creditNum
total = 0
#find the length of the number
i = len(str(cred))
if i == 15 or i == 13:
    for x in range (i):
        #find the last number of the credit card
        number = int(cred % 10)
        #remaining numbers of the creditcard
        cred = int(cred/10)
        #Multiply every other number by 2 and add the components
        if x % 2 == 0:
            total = total + number
        else:
            number = number * 2
            total = total + int(number % 10) + number // 10
elif i == 16:
    for x in range (i):
        # find last number
        number = int(cred % 10)
        # remaining number of the credit card
        cred = int(cred/10)
        #Multiply every other number by 2 and add the components
        if x % 2 != 0:
            number = number * 2
            total = total + int(number % 10) + number // 10
        else:
            total = total + number
#Checking validity and card type
if total % 10 == 0:
        if i == 13:
            print('Visa')
        elif i == 15:
            print('AmEx')
            #find the 1st number
        elif int(creditNum / 1000000000000000) == 4:
            print('Visa')
            #find the 1st 2 numbers
        elif int(creditNum / 100000000000000) >= 51 and int(creditNum / 100000000000000) <= 55 :
            print('MasterCard')
        else:
            print('Invalid')
else:
    print('Invalid')
        
