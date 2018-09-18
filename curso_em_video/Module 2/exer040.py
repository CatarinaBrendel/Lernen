n1 = float(raw_input("Enter here first grade: > "))
n2 = float(raw_input("Enter here second grade: > "))
media = (n1 + n2) / 2

if media <= 5.0:
    print "Your mean was: {:.1f}. You failed this Subject, I'm sorry!".format(media)
elif media > 5.0 and media <= 6.9:
    print "Your mean was: {:.1f}. You need to take another exam!".format(media)
else:
    print "Your mean was: {:.1f}. You passed this Subject! Congratulations!!".format(media)