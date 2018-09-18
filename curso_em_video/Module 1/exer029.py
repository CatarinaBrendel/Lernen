auto = float(raw_input("Schreiben Sie hier die Geschwindigkeit(kmh): > "))

if auto > 80:
    print "\033[1;31mSie sind schnell gefahren und jetzt mussen Sie {} Euros bezahlen!\033[m".format((auto - 80) * 7.00)

print "Guten Tag!"