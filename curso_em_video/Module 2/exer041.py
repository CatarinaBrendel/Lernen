from datetime import date

print "\033[1;32m-=\033[m" * 20
print"   Bem-Vindo a Federacao de Natacao"
print "\033[1;32m-=\033[m" * 20
print' '

print"Deixe-me selecionar sua categoria"

idade = int(raw_input("Diga-me o ano em que nasceu: > "))
idadea = date.today().year - idade

print "Voce agora tem {} anos".format(idadea)

if idadea <= 9:
    print "Sua categoria e: MIRIM"
elif idadea <=14:
    print "Sua categoria e: INFANTIL"
elif idadea <= 19:
    print "Sua categoria e: JUNIOR"
elif idadea <= 25:
    print "Sua categoria e: SENIOR"
else:
    print "Sua categoria e: MASTER"
