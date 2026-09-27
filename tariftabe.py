import os
os.system('cls')


def suming(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result


numberss = 1, 2, 3, 4

print(suming(1, 2, 3, 4))


def user_save(**user):

    print(user)


user_save(name="sara", age=22, id=1)
