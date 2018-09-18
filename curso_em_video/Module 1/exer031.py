print "\033[36m-=\033[m" * 25
print "                 Lass uns fahren?"
print "\033[36m-=\033[m" * 25
entfernung = float(raw_input("Schreiben Sie hier die Entfernung (km): > "))

if entfernung <= 200:
    print "Fuer \033[1;33m{}\033[m mussen Sie \033[1;33m{:.2f}\033[m Euros bezahlen!".format(entfernung, entfernung * 0.5)
else:
    print "Fuer \033[1;33m{}\033[m mussen Sie \033[1;33m{:.2f}\033[m Euros bezahlen!".format(entfernung, entfernung * 0.45)