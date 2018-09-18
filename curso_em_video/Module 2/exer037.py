print "\033[32m-=\033[m" * 25
print "\033[30m              Calculadora Conversora\033[m"
print "\033[32m-=\033[m" * 25

numero = int(raw_input("Digite um numero inteiro: > "))

print '''Escolha agora sua opcao: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL'''

opcao = int(raw_input("Entre sua opcao: > "))

if opcao == 1:
    binario = bin(numero)
    print "Seu numero Binario e: {}".format(binario[2:])
elif opcao == 2:
    octal = oct(numero)
    print "Seu numero OCTAl e: {}".format(octal[1:])
elif opcao == 3:
    hexa = hex(numero)
    print "Seu numero em HEXADECIMAL e: {}".format(hexa[2:])
else:
    print "Entre uma opcao valida!"

