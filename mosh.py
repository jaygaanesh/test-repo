def mul(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def user_name(**info):
    print(info['subject'])


user_name(id=1, name='jay', subject='auto')

# print(mul(1,7))
