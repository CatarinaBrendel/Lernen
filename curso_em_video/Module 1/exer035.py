lado1 = float(raw_input("Diga-me um numero: > "))
lado2 = float(raw_input("Diga-me um numero: > "))
lado3 = float(raw_input("Diga-me um numero: > "))

#Formar um triangulo:

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print "Os segmentos acima podem formar um triangulo"
else:
    print "Os seguimentos acima nao podem formar um triangulo"
