students = {}
name_counts = {}
while True:
    name = input("Enter student name: ")
    if name.lower() == "done":
        break
    str_scores = input("Enter student scores: ")

    scores = []
    new_name = name
    for i in str_scores.split():
        try:
            scores.append(float(i))
        except ValueError:
            print(f"Invalid input ignored: {i}")
    if name not in name_counts:
        name_counts[name] = 2
    while new_name in students:
        new_name = name + str(name_counts[name])
        name_counts[name] += 1
    students[new_name] = scores

print(students)
