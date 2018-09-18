num = int(raw_input("Entre um numero entre 0 e 9999: > "))

print "A unidade e: {}".format(num // 1 % 10)
print "A dezena e: {}".format(num // 10 % 10)
print "A centena e: {}".format(num // 100 % 10)
print "O milhar e: {}".format(num // 1000 % 10)

