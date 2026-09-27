import os
os.system('cls')

x = int(input("first value : "))
repeats = input("number of repeats : ")
limit = int(input("limit value : "))

reshte = input("type your string : ")

for n in range(int(repeats)):
    if x >= limit:
        print("limit reached!!!".title())

        break

    x += 2
    print(f"result {n+1} : x = {x}")


else:
    print("did not reach limit")


print(25 * "*")

for y in reshte:
    print(y)

print("done")
