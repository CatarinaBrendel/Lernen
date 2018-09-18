import random
print "{:-^50}".format(" \033[36mLet's Play Jokenpo!\033[m")

list = ['stone', 'paper', 'scissors']
print """Choose an item:
[1] stone
[2] paper
[3] scissors"""
player = int(raw_input("Choose a number from the list above: > "))
if player == 1:
    playerchoice = list[0]
elif player == 2:
    playerchoice = list[1]
elif player == 3:
    playerchoice = list[2]
else:
    playerchoice = 'invalid'
    print "You chose an invalid number. Try again!"
print "You chose \033[32m{}\033[m".format(playerchoice)

computer = random.choice(list)
print "I chose \033[34m{}\033[m!".format(computer)

if playerchoice == computer:
    print "We are tied, let's do it again!"
elif playerchoice == list[0] and computer == list[1]:
    print "I won!!"
elif playerchoice == list[0] and computer == list[2]:
    print "Ohh! you won!!"
elif playerchoice == list[1] and computer == list[0]:
    print "Ohh! you won!!"
elif playerchoice == list[1] and computer == list[2]:
    print "I won!!"
elif playerchoice == list[2] and computer == list[0]:
    print "I won!!"
elif playerchoice == list[2] and computer == list[1]:
    print "Ohh! you won!!"
