from datetime import date

print ".x" * 20
print "  Is it time for the Military Service?"
print ".x" * 20

year = int(raw_input("Enter here in which year you were born: > "))
sex = str(raw_input("Enter your sex: > ")).strip()
age = date.today().year - year
futurage = year + 18

print "Who was born in {} is 18 years old in {}".format(year, futurage )
print "You are {} years old".format(age)

if sex in ('masculino'):
    if age < 18:
        print "You have {} years left before joining the Army".format(18 - age)
    elif age == 18:
        print "The time has come! Join the Military Service now!!"
    else:
        print "You're not yet in Service? You're behind it {} year(s)!!".format(age - 18)
else:
    print "For you Military Service is not mandatory!"