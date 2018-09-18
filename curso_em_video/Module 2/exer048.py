sum = 0
cont = 0
for i in range(1, 501, 2):
        if i % 3 == 0:
            sum += i
            cont += 1
print "The sum of {} numbers is: {}".format(cont, sum)