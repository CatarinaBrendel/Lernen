print ("-=" * 25)
dist = float(raw_input("Enter here how many Km has been driven: > "))
dias = int(raw_input("Enter here how many days since you've rented: > "))
print ("-=" * 25)

print (" ")

print ("You'll have to pay: {}Euros!".format((dias * 60) + (dist * 0.15)))