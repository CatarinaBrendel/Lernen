print "{:-^50}".format(" \033[33mArithmetic Progression\033[m ")
num = int(raw_input("First number: >  "))
r = int(raw_input("By how much should it increase: > "))
n = int(raw_input("How many iteration should I present you? > "))
c = 0
while c != n:
    print num,
    num = num + r
    c += 1