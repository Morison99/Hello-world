sentence = input("sentence : ")+" "

sentence_2 = []
sent_2 = ""
lengths = []

for i in sentence:
    if i != " ":
        sent_2 += i
    else:
        sentence_2.append(sent_2)
        sent_2 = ""

for i in range(len(sentence_2)):
    lengths.append(len(sentence_2[i]))
print(lengths)

biggest_length = 0
biggest_index = 0


for i in range(len(lengths)):
    if lengths[i] > biggest_length:
        biggest_length = lengths[i]
        biggest_index = i

sentence_2.remove(sentence_2[biggest_index])
lengths.remove(lengths[biggest_index])

biggest_length = 0
biggest_index = 0

for i in range(len(lengths)):
    if lengths[i] > biggest_length:
        biggest_length = lengths[i]
        biggest_index = i

print("second biggest : ", sentence_2[biggest_index])
