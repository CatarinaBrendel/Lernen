total = countprice = less = countless = 0
bilig = " "
print "{:=^80}".format(" Bilig Geschaeft ")
while True:
    name = str(raw_input("Product Name: ")).strip().lower()
    price = float(raw_input("Price E$: "))
    print "-" * 80
    countless += 1
    total += price
    if price > 1000:
        countprice += 1
    if countless == 1:
        less = price
        bilig = name
    else:
        if price < less:
            less = price
            bilig = name
    more = " "
    while more not in "YN":
        more = str(raw_input("Do you want to keep shopping? [Y/N]: ")).strip().upper()[0]
    if more == "N":
        break
print "-" * 80
print "You have spent the total amount of E${:.2f}".format(total)
print "You bought {} products that costs more than E$1.000".format(countprice)
print "The cheapest product was {} and costed E${:.2f}".format(bilig, less)
print "End"
