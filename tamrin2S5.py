# TAMRIN FASLE 5 JALASE AKHAR


sentence = "pppppythonnn interview question"

# ravesh aval : revesh khodam
dic = dict()
for a in sentence:
    dic[a] = sentence.count(a)

max_value = max(dic.values())

for a in range(max_value, 0, -1):
    for key, val in dic.items():
        if val == a:
            print(key, val)

print(25*("*"))

# ravesh dovom : tarkib ravesh ostd ba tamrin akhar


def frequency(item):
    frequency = {}
    for char in item:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def sorted_frequency(item):
    fre = frequency(item)
    sorted_frequency = sorted(fre.items(),
                              key=lambda kv: kv[1],
                              reverse=True)

    for char, count in sorted_frequency:
        print(char, count)


sorted_frequency(sentence)
