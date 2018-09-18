import random

n1 = raw_input("Emter a name here: > ")
n2 = raw_input("Enter a second name: > ")
n3 = raw_input("Enter a third name: > ")
n4 = raw_input("Enter a fourth name: > ")

list = [n1, n2, n3, n4]

random.shuffle(list)

print "The order of the names is: {}".format(list)