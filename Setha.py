nums = [1, 2, 3, 4, 5, 1, 2, 6, 2, 7, 3, 7]

first = set(nums)
second = {1, 8, 12, 15}

print(first)

print(first & second)
print(first | second)
print(first ^ second)
print(first - second)

second.add(288)
print(second)

x = set("hello")
y = set("help")

print(x ^ y)
