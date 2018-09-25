my_list = []
mode = True
while mode:
    num = (int(input("Enter a number: ")))
    if num not in my_list:
        my_list.append(num)
    else:
        print("You already gave me that number.")

    option = (str(input("Would you like to add more? [Y/N]: ")).strip().upper()[0])
    if option not in "YN":
        print("Enter a valid input [Yes or No]")
        option = (str(input("Would you like to add more? [Y/N]: ")).strip().upper()[0])
    if option in "N":
        mode = False
my_list.sort()
print('=' * 38)
print(f"The numbers inputed were: {my_list}")