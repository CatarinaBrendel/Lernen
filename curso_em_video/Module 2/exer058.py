from random import randint

print "{:-^100}".format(" \033[31mCan you guess which Number I just thought? a hint: it's between 0 and 3?\033[m ")

computer = randint(0,10)
count = 0
correct = False

while not correct:
    player = int(raw_input("Write here your guess: > "))
    count += 1
    if player == computer:
        correct = True
    else:
        if player < computer:
            print "Not that one... It's bigger than that!"
        elif player > computer:
            print "Not really... It's smaller than that!"
print "That's right! I thought on the number {}!".format(computer)
print "And you took {} tries to get it right!".format(count)


