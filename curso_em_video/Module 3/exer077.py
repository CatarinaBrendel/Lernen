words = ('house', 'bird', 'play', 'games', 'victory')

for i in words:
    print "\nIn the word {} there are ".format(i),
    for letter in i:
        if letter in "aeiou":
            print letter,
