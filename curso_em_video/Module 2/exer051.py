num = int(raw_input("Digite o primeiro valor de sua PA: > "))
razao = int(raw_input("Digite aqui a razao de sua PA: > "))
for n in range(num, (num + (10 - 1) * razao), razao):
    print n