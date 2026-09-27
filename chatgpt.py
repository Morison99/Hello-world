
# def second_max(numbers):
#     biggest = numbers[0]
#     second_biggest = numbers[0]
#     for i in numbers:
#         if i > biggest:
#             second_biggest = biggest
#             biggest = i
#         elif i > second_biggest:
#             if i != biggest:
#                 second_biggest = i
#     return biggest, second_biggest


# # مشکل اعداد تکراری؟؟؟؟؟
# print(second_max([-5, -3, -2, -1, -1, -1, -9]))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# squared_positive = [i**2 for i in numbers if i % 2 == 0 and i > 0]

# cubed_evens = {i: i**3 for i in numbers if i % 2 == 0}
# scores = {
#     "Ali": 18,
#     "Reza": 12,
#     "Sara": 19,
#     "Mina": 9,
#     "Nima": 16
# }

# higher_than15 = {key: value+2 for key, value in scores.items() if value >= 15}


# print(list(filter(lambda x: x % 2 == 0, numbers)))
# names = ["ALI", "REZA", "MORTEZA"]
# numbers = [10, 25, 30, 40, 50]
# with open("name.txt", "w") as file:
#     for number in numbers:
#         file.write(str(number)+"\n")

# with open("number.txt") as file:
#     lines = file.readlines()

# numbers = []
# for line in lines:
#     if line.strip():
#         numbers.append(int(line.strip()))


# def average(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total/len(numbers)
# print(average(numbers))

# names = ["Ali", "Reza"]
# with open("name.txt", "w") as file:
#     for name in names:
#         file.write(name+"\n")


# new_names = ["Morteza", "Sara"]
# with open("name.txt", "a") as file:
#     for name in new_names:
#         file.write(name+'\n')

# with open("name.txt") as file:
#     file = file.readlines()

# names = []
# for name in file:
#     if name.strip():
#         names.append(name.strip().upper())


# print(names)

# with open("upper_names.txt", "w") as file:
#     for name in names:
#         file.write(name + "\n")


# with open("numbers.txt") as file:
#     nums = file.readlines()


# numbers = []
# for number in nums:
#     condition = number.strip()
#     if condition and int(condition) > 20:
#         numbers.append(int(condition))

# with open("big_numbers.txt", "w") as file:
#     for num in numbers:
#         file.write(str(num) + "\n")

# print(numbers)
