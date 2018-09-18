print "Vamos formar um triangulo"
print ""
a = int(raw_input("Diga-me um numero: "))
b = int(raw_input("Diga-me um segundo numero: "))
c = int(raw_input("Diga-me um terceiro numero: "))

ab = a + b
ac = a + c
bc = b + c

if a < bc and b < ac and c < ab:
    print "Esses numeros podem formar um triangulo!"

    if ab == ac == bc:
        print "Os lados {}, {} e {} formam um triangulo EQUILATERO".format(a, b, c)
    elif ab != ac and ab != bc and bc != ac:
        print "Os lados {}, {} e {} formam um triangulo ESCALENO".format(a, b, c)
    else:
        print "Os lados {}, {} e {} formam um triangulo ISOSCELES".format(a, b, c)

else:
    print "Esses numeros nao podem formar um triangulo!"