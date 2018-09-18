print "{:=^50}".format(" \033[34mFibonacci Sequence\033[m ")
print "Give me the numbers of elements you want to be displayed"
n = int(raw_input("Number: > "))
count = 3
f1 = 0
f2 = 1
print f1, f2,
# while count <= n:
#    f3 = f1 + f2
#    print f3,
#    f1 = f2
#    f2 = f3
#    count += 1
#    f1 = f2
#    f2 = f1 + f2

while count <= n:
   print f1 + f2,
   f1, f2 = f2, f1 + f2
   count+= 1
# This simplified code represents the same as stated in the loop above, it just uses
# some pythonic way of calling and atributing values