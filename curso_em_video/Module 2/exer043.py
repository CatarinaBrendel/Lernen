print "\033[35m-=\033[m" * 20
print "          Calculadora de IMC"
print "\033[35m-=\033[m" * 20

peso = float(raw_input("Diga-me seu peso (Kg): > "))
altura = float(raw_input("Diga-me sua altura (m): > "))
imc = peso / altura ** 2

if imc < 18.5:
    print "Com um IMC de {:.1f}, voce esta \033[1;31mAbaixo do Peso\033[m!".format(imc)
elif imc < 25:
    print "Com um IMC de {:.1f}, voce esta com o \033[32mPeso Ideal\033[m!".format(imc)
elif imc < 30:
    print "Com um IMC de {:.1f}, voce esta com \033[1;31mSobrepeso\033[m!".format(imc)
elif imc < 40:
    print "Com um IMC de {:.1f}, voce esta com \033[1;31mObesidade\033[m!".format(imc)
else:
    print "Com um IMC de {:.1f}, voce esta com \033[1;31mObesidade Morbida\033[m!".format(imc)
