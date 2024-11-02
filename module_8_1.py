def add_everything_up(x,y):
    try:
        result = x + y
    except TypeError:
        result = str(x) + str(y)
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
