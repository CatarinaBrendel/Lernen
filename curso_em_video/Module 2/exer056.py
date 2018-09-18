sumage = count = mean = older = younger = 0
nameold = " "
for p in range(1,5):
    print "{:-^20}".format(" Data ")
    name = str(raw_input("Name: ")).strip().lower()
    sex = str(raw_input("Sex [M/F]: ")).strip().upper()[0]
    age = int(raw_input("Age: "))
    sumage += age
    if p == 1 and sex in "M":
        older = age
        nameold = name
    if sex in "M" and age > older:
        older = age
        nameold = name
    if sex in "F" and age < 20:
        younger = age
        count += 1

mean = sumage/4
print "The mean of all ages is: {}".format(mean)
print "The oldest Man is called {} and is {} years old".format(nameold, older)
print "There are {} women with less than 20 years".format(count)
