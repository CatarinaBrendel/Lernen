print "\033[31mx.\033[m" * 30
print "\033[32m                  Die Gehaltserhoehung!\033[m"
print "\033[31mx.\033[m" * 30

gehalt = float(raw_input("\033[32m          Schreiben Sie hier dein Gehalt: > \033[m"))

if gehalt > 1250:
    print "Dein Gehalt nachsten Monat ist: {:.2f}".format(gehalt + (gehalt * 0.1))
else:
    print "Dein Gehalt naechsten Monat ist: {:.2f}".format(gehalt + (gehalt * 0.15))
