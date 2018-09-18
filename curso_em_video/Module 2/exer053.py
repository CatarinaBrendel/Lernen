print "Enter a Phrase and I'll tell you if it is a Palindrome or not"
sentence = str(raw_input("Your phrase here: > ")).strip().lower().replace(' ', '')
pal = ""
for i in sentence:
    pal = i + pal
if pal == sentence:
    print "'{}' is a palindrome!".format(sentence)
else:
    print "'{}' is NOT a palindrome!".format(sentence)

