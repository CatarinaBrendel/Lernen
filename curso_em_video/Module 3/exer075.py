numbers = []
count = 0
for i in range(0, 4):
    numbers.append(int(raw_input("Enter {} number: > ".format(i+1))))
my_numb = tuple(numbers)

print "{:-^45}".format(" Data ")

print "My Tuple: {}".format(my_numb)

print "a) The Number 9 came up {} time(s).".format(my_numb.count(9))

if 3 in my_numb:
    print "b) The Number 3 is in position {}".format(my_numb.index(3))
else:
    print "b) There's no Number 3 in my tuple!"

for n in my_numb:
    if n > 0:
        if n % 2 == 0:
            count += 1

print "c) There are {} Even numbers in my tuple.".format(count)
