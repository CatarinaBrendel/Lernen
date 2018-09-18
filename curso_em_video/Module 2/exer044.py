print"{:=^55}".format(' \033[34mLojas Descontao\033[m ')

preco = float(raw_input("Digite aqui o preco em R$ a ser calculado: > "))

print """Escolha aqui a forma de pagamento:
[1] a vista em dinheiro ou cheque para ter 10% de desconto
[2] a vista em cartao para 5% de desconto
[3] em ate 2x no cartao sem juros e sem descontos
[4] em 3x no cartao com 20% de juros ao mes"""
forma = int(raw_input("Digite aqui o numero correspondente a sua escolha: > "))
print "Voce escolheu a opcao {}".format(forma)

if forma == 1:
    total = preco - (preco * 10/100)
elif forma == 2:
    total = preco - (preco * 5/100)
elif forma == 3:
    total = preco / 2
elif forma == 4:
    total = preco + (preco * 20/100)
    parcela = int(raw_input("Em quantas parcelas? : > "))
    totalparc = total / parcela
    print "O valor de cada parcela sera: R${:.2f}".format(totalparc)
else:
    total = preco
    print "Voce selecionou um opcao invalida. Tente novamente!"

print "Sua compra no valor de R${:.2f}, com a opcao escolhida custara no total R${:.2f}".format(preco, total)
