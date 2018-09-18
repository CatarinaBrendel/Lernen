sex = str(raw_input("Enter your sex: ")).lower()
while sex not in "malefemale":
    print "You haven't typed a valid answer"
    sex = str(raw_input("Enter your sex: ")).upper()
    print "Please type it again"
print "Information registered. Thank you for taking part in it!"