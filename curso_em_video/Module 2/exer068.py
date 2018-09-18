from random import randint
count = 0

print ("{:=^88}".format(" \033[32mEven or Odd?\033[m "))
print """Let's play a small game of Even or Odd. Tell me a Number and we will compare.
The game is over when you, Player, loose!"""
print "-" * 80

while True:
   player = int(input("Enter a number: > "))
   computer = randint(0,10)
   summe = player + computer
   option = 0
   while option not in [1,2]:
       print"""Choose from the Menu:
       [1] EVEN
       [2] ODD"""
       option = int(input("Your choice: > "))
       print "-" * 80
   print (" You played {} and I played {}. Our sum was {}".format(player, computer, summe))
   if option == 1:
       if summe %2 == 0:
           print "You chose EVEN and our sum was EVEN. You WON!"
           count += 1
       else:
           print "You chose EVEN and our sum was ODD. You LOST :("
           break
   elif option == 2:
       if summe %2 == 1:
           print "You chose ODD and our sum was ODD. You WON!"
           count += 1
       else:
           print "You chose ODD and our sum was EVEN. You LOST :("
           break
   print "Let's play again!"
   print "-" * 80
print "-" * 80
print "You won {} times.".format(count)
print "Game Over!"