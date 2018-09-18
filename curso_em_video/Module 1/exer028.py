import random

print ("x-" * 30)

print ("  Voce consegue advinhar que numero entre 0 e 5 eu pensei?")

print ("x-" * 30)

num = random.randint(0,6)

num1 = int(raw_input("Faca aqui sua aposta: > "))

if num == num1:
    print ("Voce e bom!!")
else:
    print "Pensei no {}. Nao foi dessa vez. Tente novamente!".format(num)