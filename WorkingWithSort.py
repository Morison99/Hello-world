# names = ["Ali", "Reza", "Sara", "Mina"]
# scores = [16, 9, 19, 14]

# students = list(zip(names, scores))
# sort_orders = sorted(students,
#                      key=lambda x: x[1], reverse=True)
# for counter, (name, score) in enumerate(sort_orders, start=1):
#     print(f"{counter}. {name} : {score}")

# python_students = {"Ali", "Reza", "Sara", "Mina"}
# ai_students = {"Sara", "Mina", "Hossein", "Amir"}
# py_only = python_students - ai_students
# print(py_only)
# one_of_both = ai_students.union(python_students)
# print(one_of_both)

student_ranking = [
    ("Ali", 18),
    ("Reza", 18),
    ("Sara", 18),
    ("Morteza", 16),
    ("Mehdi", 14),
    ("Hadi", 14)
]
# counter = 0
# pre_value = None
# rank = 1
# for key, value in student_ranking:

#     if value != pre_value:
#         print(f"{rank}. {key} : {value}")
#         counter = 0
#     else:
#         print(f"{rank - counter}. {key} : {value}")
#     rank += 1
#     counter += 1
#     pre_value = value

counter = 1
rank = 1
pre_value = None

for key, value in student_ranking:

    if value != pre_value:
        rank = counter
    print(f"{rank}. {key} : {value}")

    counter += 1
    pre_value = value
