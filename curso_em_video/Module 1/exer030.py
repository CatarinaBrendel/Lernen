num = int(raw_input("Schreiben Sie hier einen Nummer: > "))

if num % 2 == 0:
    print "Sie haben eine \033[1;34mgerade\033[m Zahl geschrieben!"
else:
    print "Sie haben eine \033[1;32mungerade\033[m Zahl geschrieben!"