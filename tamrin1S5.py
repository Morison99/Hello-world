dic = dict(a=5, t=10, u=8, v=10, w=8)


number = 0
dic2 = dict()

for key, val in dic.items():
    if val >= number:
        number = val

for key, val in dic.items():
    if val == number:
        print(key)
