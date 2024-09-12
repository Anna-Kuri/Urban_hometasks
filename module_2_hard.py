while True:
    number = int(input("You don't have much time left! What's the first number? "))

    if number >= 3 and number <= 20:
        password = []
        for i in range(1, 21):
            for j in range(1, 21):
                if i in password and j in password:
                    pass
                else:
                    if i != j:
                        pair = i + j
                        if number % pair == 0:
                            password.append(i)
                            password.append(j)
                            continue

        print(f'Your password is: {"".join(str(x) for x in password)} Hurry up!')
        break
    else:
        print('You got it wrong! The number can be only in range from 3 to 20. Check the number again')