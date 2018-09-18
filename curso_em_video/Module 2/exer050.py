print "Enter 6 numbers and I'll give you the total sum of only \033[4;32mthe Even\033[m ones"
sum = 0
for n in range(1, 7):
    num = int(raw_input("Enter the {} number: > ".format(n)))
    if num % 2 == 0:
        sum += num
print "The Sum of the inputed EVEN numbers is {}".format(sum)