my_list = list()

for i in range(0, 5):
    my_list.append(int(input("Give me a Number: ")))

print(f"You have entered {my_list}")
print(f"The biggest number was {max(my_list)} in position ", end='')
for i, v in enumerate(my_list):
    if v == max(my_list):
        print(f"{i}...", end="")
print()
print(f"The smallest value was {min(my_list)} in position ", end='')
for i, v in enumerate(my_list):
    if v == min(my_list):
        print(f"{i}...", end='')
