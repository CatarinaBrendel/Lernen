import math

a = float(raw_input("Qual o compirmento do cateto adjacente? > "))
b = float(raw_input("Qual o comprimento do cateto adjacente? > "))

print "O valor ha hipotenusa e {}".format((a ** 2 + b ** 2) ** 0.5)

print "O valor da hipotenusa e {}".format(math.hypot(a, b))