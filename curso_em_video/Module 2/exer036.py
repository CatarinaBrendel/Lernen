print "\033[31m.x\033[m" * 25
print "              Avaliando Emprestimos"
print "\033[31m.x\033[m" * 25

valor = float(raw_input("Diga-me o valor da casa: > "))
salario = float(raw_input("Diga-me o valor do seu salario: > "))
tempo = int(raw_input("Em quanto tempo (em meses) pretende pagar? > "))
prestacao = valor // (salario * tempo)

if prestacao < salario * 0.3:
    print "Sua prestacao tera o valor mensal de R${}, dessa forma seu emprestimo foi CONCEDIDO".format(prestacao)
else:
    print "Seu credito nao foi aprovado pois a prestacao R${} supera 30% de seu salario".format(prestacao)