frase = str(raw_input("Escreva uma frase aqui: > ")).strip().lower()

print "Nesta frase existem exatamente {} letra 'a'".format(frase.count('a'))
print "o primeiro 'a' esta na posicao {} e o segundo na posicao {}!".format(frase.index('a')+1, frase.rindex('a')+1)