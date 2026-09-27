def is_prime(number):

    if number > 1:

        x = True
        for n in range(2, number):

            if (number % n) != 0:
                x = x and True

            else:
                x = x and False
        return x

    else:
        return False


def show_prime(num1, num2):

    result = ""
    for a in range(num1, num2+1):
        if is_prime(a):
            result += (" " + str(a))

    return result


print(show_prime(-5, 23))
