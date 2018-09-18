n = sum = count = max = min = 0
keep = ""
while keep != "n":
    n = int(raw_input("Enter a number: > "))
    sum += n
    count += 1
    if count == 1:
        max = min =  n
    else:
        if n > max:
            max = n
        if n < min:
            min = n
    keep = str(raw_input("Want to give another number [y/n]? > ")).strip().lower()[0]
    if keep not in "yn":
        print "Enter a valid option!"
print "You gave me {} numbers".format(count)
print "Their sum is: {} and their mean is: {}".format(sum, float(sum/count))
print "The biggest number is {} and the smallest {}!".format(max, min)




