mylist = []
even = []
odd = []

while True:
    mylist.append(int(input('Give me a Number: ')))
    option = str(input('Do you want to add more [Y/N]? ')).strip().upper()[0]
    if option == 'N':
        break
    elif option != 'YN':
        print('You have entered an invalid input.')
        option = str(input('Do you want to add more [Y/N]? ')).strip().upper()[0]
for n in mylist:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
mylist.sort()

print('-=' * 35)
print(f'You gave me {len(mylist)} numbers: {mylist}')
print(f'From the Numbers you gave me, these are the Even: {even}')
print(f'And these are the Odd: {odd}')
