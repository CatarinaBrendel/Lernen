print '-' * 35
print '{:^35}'.format("ATM")
print '-' * 35

amount = int(raw_input("How much you want to withdraw? E$ "))
bill = 500
totbill = 0

while True:
    if amount >= bill:
        amount -= bill
        totbill += 1
    else:
        if totbill > 0:
            print "Total of {} bills of E$ {}".format(totbill, bill)
        if bill == 500:
            bill = 100
        elif bill == 100:
            bill = 50
        elif bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 5
        elif bill == 5:
            bill = 1
        totbill = 0
        if amount == 0:
            break
print '-' * 35
print"Thank you for trusting our services. Have a nice day!"