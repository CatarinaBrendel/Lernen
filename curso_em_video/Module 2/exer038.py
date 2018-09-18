a = float(raw_input("Enter a number here: > "))
b = float(raw_input("Enter a second number here: > "))

if a > b:
    print "{} is the biggest number".format(a)
elif a < b:
    print "{} is the biggest number".format(b)
else:
    print "{} and {} are equals!".format(a, b)