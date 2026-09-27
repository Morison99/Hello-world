# try:
#     number = int(input("type the number : "))
#     print(100/number)
# except ValueError:
#     print("you didnt tye a number")
# except ZeroDivisionError:
#     print("Zero not valid")

# try:
#     with open("numbers.txt") as file:
#         lines = file.readlines()

#     numbers = []
#     for nums in lines:
#         if nums.strip():
#             numbers.append(int(nums.strip()))
#     print(numbers)
# except FileNotFoundError:
#     print("File Does Not Exist")
# except ValueError:
#     print("the file contains strings")

# try:
#     number = int(input("type the number : "))
# except ValueError:
#     print("you havnt entered a number")
# else:
#     print(number**2)

# print("program finished")

with open("numbers.txt") as file:
    lines = file.readlines()


numbers = []
for number in lines:
    try:
        if number.strip():
            numbers.append(int(number.strip()))
    except ValueError:
        pass
print(numbers)


def min_max_avg(numbers):
    min = numbers[0]
    max = numbers[0]
    total = 0

    for i in numbers:
        total += i
    avg = total/len(numbers)

    for i in numbers:
        if i > max:
            max = i

    for i in numbers:
        if i < min:
            min = i

    return min, max, avg


min, max, avg = min_max_avg(numbers)

print(f"min = {min} , max = {max}, average = {avg}")
