print("{:=^45}".format(" Futball Now "))

team = ('Sao Paulo', 'Internacional', 'Palmeiras', 'Flamengo', 'Gremio', 'Atletico-MG', 'Cruzeiro',
         'Corinthians', 'Santos', 'Fluminense', 'Atletico-PR', 'America-MG', 'Vitoria', 'Bahia', 'Botafogo',
         'Chapecoense', 'Ceara', 'Vasco', 'Sport', 'Parana Clube')
print "The first fives are: ", team[:5]
print "The last four are: ", team[17:]
print "In alphabetical order we have: ", sorted(team)
print "The Chapecoense team is in {}th position!".format(team.index("Chapecoense")+1)
