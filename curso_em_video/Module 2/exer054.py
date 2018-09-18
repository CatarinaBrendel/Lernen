from datetime import date
countold = 0
countjung = 0
print "Give me "
for i in range(1, 8):
    year = int(raw_input("In which year the {} person was born?: ".format(i)))
    old = date.today().year - year
    if old <= 18:
        countjung += 1
    else:
        countold += 1
print "Here there are {} more than 18 y/o people and {} less than 18 y/o people!".format(countalt, countjung)
