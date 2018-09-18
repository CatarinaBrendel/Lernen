n = summe = count = 0
while True:
    n = int(input("Schreiben Sie hier einen Number [999 halt das Programm]: > "))
    if n == 999:
        break
    summe += n
    count += 1

print ("{:=^40}".format(" Information "))
print ("Sie haben {} Numbern geschrieben".format(count))
print ("Die Summe von diesen Numbern ist: {}".format(summe))

