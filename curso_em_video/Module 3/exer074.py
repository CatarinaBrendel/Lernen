from random import randint
numberslist = []
for i in range(0, 6):
    rand = randint(0, 10)
    numberslist.append(rand)
numberstup = tuple(numberslist)
print numberstup
print "The biggest number is: {}".format(max(numberstup))
print "The smallest value is {}".format(min(numberstup))
