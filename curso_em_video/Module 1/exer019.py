import random

n1 = raw_input("Enter here a name: > ")
n2 = raw_input("Enter here a second name: > ")
n3 = raw_input("Enter here a third name: > ")
n4 = raw_input("Enter here a fourth name: > ")

list = [n1, n2, n3, n4]

print "By the power of statistics I choose {}!".format(random.choice(list))