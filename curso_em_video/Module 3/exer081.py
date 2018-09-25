mylist = []

while True:
    num = int(input('Write a Number: '))
    mylist.append(num)

    option = str(input('Want to continue? [Y/N]:  ')).strip().upper()[0]
    if option in 'No':
        break
    if option not in 'NoYes':
        print('Enter a valid input')
        option = str(input('Want to continue? [Y/N]:  ')).strip().upper()[0]

mylist.sort(reverse=True) 

print(f'You have entered {len(mylist)} numbers.')
print(f'The numbers in decreasing order is {mylist}')

if 5 in mylist:
    print('The number 5 is in the List!')
else:
    print('There is no number 5 in the List!')