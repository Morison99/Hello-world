import os
os.system('cls')

current_year = int(input("current year: "))
date_of_birth = input("date of birth(yyyy/mm/dd): ")

birth_year = int(date_of_birth[0:4])
birth_month = int(date_of_birth[5:7])
birth_day = int(date_of_birth[8:])
age = current_year - birth_year

print(10 * "_")
print("birth year = ", birth_year)
print("birth month = ", birth_month)
print("birth day = ", birth_day)
print("your age = ", age)
print("It is on GitHub")
print("This is a test branch")
