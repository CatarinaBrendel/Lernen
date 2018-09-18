print "{:=^50}".format(" \033[34mWilkomen!\033[m ")
num1 = int(raw_input("Geben Sie mir einen Nummer: "))
num2 = int(raw_input("Geben Sie mir einen anderen Nummer: "))
option = 0

while option != 5:
    print """{:-^50}
[1] summieren
[2] multiplizieren
[3] grosser
[4] neuer Nummer
[5] End des Programmes""".format(" \033[35mMenu!\033[m ")
    option = int(raw_input("Waehlen Sie eine Option aus: "))
    if option == 1:
        print "Die Summe von {} + {} ist: {}".format(num1, num2, num1 + num2)
    elif option == 2:
        print "Der Erfolg von {} * {} ist: {}".format(num1, num2, num1 * num2)
    elif option == 3:
        if n1 > n2:
            grosser = n1
        else:
            grosser = n2
        print "{} ist der grossest Nummer!".format(grosser)
    elif option == 4:
        print "Geben Sie mir andere Nummern:"
        num1 = int(raw_input("Erster Nummer: "))
        num2 = int(raw_input("Zweiter Nummer: "))
    elif option == 5:
        print "End das Programmes..."
    else:
        print "Geben Sie mir eine richtige Option"
    print "-"* 50
print "Vielen Dank!"