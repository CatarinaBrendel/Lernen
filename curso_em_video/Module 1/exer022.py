name = str(raw_input("Enter a name here: > ")).strip()

print "A study of your name shows:"

print "Your name in upper case is: {}".format(name.upper())

print "Your name in lower case is: {}".format(name.lower())

print "Your name has {} letters!".format(len(name) - name.count(' '))

print "Your first name has {} letters! ".format(name.find(" "))