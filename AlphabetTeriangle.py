import string

alphabet = string.ascii_uppercase

b = 0
for a in range(1, 11, 2):
    print(alphabet[b:b+a].center(10))
    b += a

# c = list(range(1, 11, 2))
# print(c)
