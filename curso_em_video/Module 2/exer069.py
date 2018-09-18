print "{:=^80}".format(" People Database ")
sumage = summale = sumfemale = 0

while True:
    age = int(raw_input("Enter your age: "))
    sex = " "
    while sex not in "MF":
        sex = str(raw_input("Enter your sex [M/F]: ")).strip().upper()[0]
        print "-" * 80
    if age >= 18:
        sumage +=1
    if sex == "M":
        summale += 1
    if age < 20 and sex == "F":
        sumfemale += 1
    more = " "
    while more not in "YN":
        more = str(raw_input("Want to Insert more Data [Y/N]: ")).strip().upper()[0]
        print "-" * 80
    if more == "N":
        break
print "-" * 80
print "There are {} people with more than 18 years old".format(sumage)
print "There are {} male in this Data".format(summale)
print "There are {} women with less than 21 years old".format(sumfemale)
print "End"