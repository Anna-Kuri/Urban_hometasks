my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    value = my_list[index]

    index += 1

    if value > 0:
        print(value)
    elif value == 0:
        continue
    else:
        break
