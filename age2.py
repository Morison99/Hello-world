age = int(input("AGE : "))

if age < 13:
    print("child")
elif 13 <= age < 20:
    print("teenage")
elif 20 <= age < 110:
    print("adult")
else:
    print("YOU MUST BE DEAD by NOW")
