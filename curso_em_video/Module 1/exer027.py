name = str(raw_input("Digite um nome composto: > ")).strip()

name1 = name.split()

print ("O primeiro no e {} e o ultimo e {}".format(name1[0], name1[len(name1)-1]))