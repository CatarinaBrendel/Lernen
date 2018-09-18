min = 0
max = 0
for i in range(1,6):
    weight = float(raw_input("Enter here the {} weight (Kg): ".format(i)))
    if i == 1:
        max = weight
        min = weight
    else:
        if weight > max:
            max = weight
        if weight < min:
            min = weight
print "The heaviest person has {}Kg and the lightest person has {}Kg".format(max, min)