print "Write a number and I'll tell you if it is a prime or not!"
num = int(raw_input("Enter a number: > "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print "\033[31m",
    else:
        print "\033[32m",
    print "{}".format(c),
print "\n\033[mThe Number {} was devided {} times".format(num, total)
if total == 2:
    print "The Number {} is PRIME!".format(num)
else:
    print "The Number {} is NOT PRIME".format(num)

