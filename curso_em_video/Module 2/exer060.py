from math import factorial
number = int(raw_input("Enter a number: "))
print "The Factorial of {} is {}".format(number, factorial(number))
print""

print "{:=^50}".format(" Manual Version ")
c = number
f = 1
while c > 0:
    print "{}".format(c),
    print "x" if c > 1 else "= {}".format(f),
    f *= c
    c -= 1
print "\nThe Factorial of {} is {}".format(number,f)