num1 = int(raw_input("Schreiben Sie eine Nummer: > "))
num2 = int(raw_input("Schreiben Sie eine Nummer: > "))
num3 = int(raw_input("Screiben Sie eine Nummer: > "))

gross = num1
if num2 > num1 and num2 > num3:
    gross = num2
if num3 > num1 and num3 > num2:
    gross = num3

klein = num1
if num2 > num1 and num2 > num3:
    klein = num2
if num3 < num1 and num3 < num2:
    klein = num3

print "{} ist am grossten!".format(gross)
print "{} ist am kleinesten".format(klein)