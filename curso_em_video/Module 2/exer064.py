print "{:=^50}".format(" \033[31mGive me numbers until 999!\033[m ")
print "[999 to make me stop!]"
n = int(raw_input("Give me a number: > "))
count = 0
summe = 0
while n != 999:
    count += 1
    summe += n
    n = int(raw_input("Give me a number: > "))
print "You gave me {} numbers and their sum is {}!". format(count, summe)

