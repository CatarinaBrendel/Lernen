my_list = []

for i in range(0, 3):
    num = int(input('Write a number: '))
    if i == 0 or num > my_list[-1]:
        my_list.append(num)
    else:
        pos = 0
        while pos < len(my_list):
            if num <= my_list[pos]:
                my_list.insert(pos, num)
                break
            pos += 1

print(my_list)