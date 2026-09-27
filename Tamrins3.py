import os
os.system('cls')


command = input("... ")
result = ""

for a in command:

    if a.lower() in "pom":
        result += "*"
    else:
        result += a

print(result)
