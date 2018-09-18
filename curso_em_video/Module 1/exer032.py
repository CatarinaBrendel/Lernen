from datetime import date

print "\033[31m-x\033[m" * 32
print "  Ich wollte dir sagen, ob ein Jahr Schaltjahr ist oder nein!"
print "\033[31m-x\033[m" * 32
print " "
print "Wenn Sie 0 geschrieben haben, gebe ich dir gerade Jahr"
jahr = int(raw_input("Schreiben Sie hier ein Jahr: > "))

if jahr == 0:
    jahr = date.today().year

if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
    print "\033[32m{}\033[m ist ein Schaltjahr!".format(jahr)
else:
    print "\033[32m{}\033[m ist kein Schaltjahr!".format(jahr)