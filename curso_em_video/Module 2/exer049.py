print "{:-^45}".format(' \033[31mTabuada\033[m ')
num = int(raw_input("Digite aqui um numero inteiro a ser multiplicado: > "))
num2 = int(raw_input("Digite aqui o valor da tabuada: > "))
for n in range(1, num2+1):
    print "{:3} x {:3} = {:3}".format(num, n, num * n)