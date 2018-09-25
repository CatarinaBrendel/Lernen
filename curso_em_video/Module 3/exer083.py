expression = str(input('Give me a mathematical expression: '))
accumulate = []
for i in expression:
    if i == '(':
       accumulate.append('(')
    elif i == ')':
        if len(accumulate) > 0:
            accumulate.pop()
        else:
            accumulate.append(')')
            break
if len(accumulate) == 0:
    print('You have a valid expression')
else:
    print('You have an invalid expression')