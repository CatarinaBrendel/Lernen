number = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
          'seventeen', 'eighteen', 'nineteen', 'twenty')

user = int(raw_input('Enter a number between 0 and 20:> '))
while user not in range(0, 21):
    print("You have entered an invalid number. Try again!")
    user = int(raw_input('Enter a number between 0 and 20:> '))
    break
if user in range(0, 21):
    print("You have typed the number {}".format(number[user]))