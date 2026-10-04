def analyze_scores(scores):
    valid_scores = [score for score in scores if 0 <= score <= 20]

    if not valid_scores:
        return {"total_valid_scores": 0, "unacceptable_scores": len(scores)}

    average = sum(valid_scores)/len(valid_scores)
    maximum = max(valid_scores)
    minimum = min(valid_scores)
    passed = sum(score >= 10 for score in valid_scores)
    unpassed = sum(score < 10 for score in valid_scores)
    valid_count = len(valid_scores)
    pass_rate = passed / valid_count * 100
    unacceptable_scores = len(scores) - valid_count

    return {
        "average_score": average,
        "maximum_score": maximum,
        "minimum_score": minimum,
        "total_passed": passed,
        "total_unpassed": unpassed,
        "pass_rate": pass_rate,
        "unacceptable_scores": unacceptable_scores,
        "total_valid_scores": valid_count
    }


def find_max(current_value, current_name, new_value, new_name):
    if current_value is None or current_value < new_value:
        current_value = new_value
        current_name = new_name
    return current_value, current_name


def find_min(current_value, current_name, new_value, new_name):
    if current_value is None or current_value > new_value:
        current_value = new_value
        current_name = new_name
    return current_value, current_name


def class_summary(students):
    best_student = None
    worst_student = None
    student_with_highest_score = None
    student_with_lowest_score = None
    best_average = None
    worst_average = None
    maximum = None
    minimum = None
    total_passed = 0
    total_unpassed = 0
    total_unacceptable_scores = 0
    sort_by_average = {}
    students_without_scores = []
    for name, scores in students.items():
        result = analyze_scores(scores)
        total_unacceptable_scores += result["unacceptable_scores"]
        if result["total_valid_scores"] == 0:
            students_without_scores.append(name)
        else:
            sort_by_average[name] = result["average_score"]
            best_average, best_student = find_max(
                best_average,
                best_student,
                result["average_score"],
                name
            )
            worst_average, worst_student = find_min(
                worst_average,
                worst_student,
                result["average_score"],
                name
            )
            maximum, student_with_highest_score = find_max(
                maximum,
                student_with_highest_score,
                result["maximum_score"],
                name
            )

            minimum, student_with_lowest_score = find_min(
                minimum,
                student_with_lowest_score,
                result["minimum_score"],
                name
            )
            total_passed += result["total_passed"]
            total_unpassed += result["total_unpassed"]

    total_valid_scores = total_passed + total_unpassed
    if total_valid_scores == 0:
        return {
            "total_valid_scores": 0,
            "students_without_scores": students_without_scores
        }
    student_ranking = sorted(sort_by_average.items(),
                             key=lambda x: x[1], reverse=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # برای اینکه به جند نفر با معدل یکسان رتبه یکسان اختصاص داده شود:
    counter = 1
    rank = 1
    pre_value = None
    ranking = []
    for key, value in student_ranking:

        if value != pre_value:
            rank = counter
            counter += 1
        ranking.append((rank, key, value))

        pre_value = value

    # ==========================================================

    overall_pass_rate = total_passed / total_valid_scores * 100
    return {"best_student": best_student, "best_average": best_average,
            "worst_student": worst_student, "worst_average": worst_average,
            "student_with_highest_score": student_with_highest_score, "highest_score": maximum,
            "student_with_lowest_score": student_with_lowest_score, "lowest_score": minimum,
            "total_passed": total_passed, "total_unpassed": total_unpassed,
            "total_unacceptable_scores": total_unacceptable_scores,
            "total_valid_scores": total_valid_scores,
            "overall_pass_rate": overall_pass_rate,
            "student_ranking": ranking, "students_without_scores": students_without_scores
            }


def print_summary(summary):

    print("===== Class Summary =====")
    print()
    print("Ranking:")

    if summary["total_valid_scores"]:
        for rank, name, average in summary["student_ranking"]:
            print(f"{rank}. {name}: {average:.2f}")
        print(summary["students_without_scores"])
        print(f"""
Best student: {summary["best_student"]}
Best average: {summary["best_average"]:.2f}

Worst student: {summary["worst_student"]}
Worst average: {summary["worst_average"]:.2f}

Highest score: {summary["highest_score"]}
Student with highest score: {summary["student_with_highest_score"]}

Lowest score: {summary["lowest_score"]}
Student with lowest score: {summary["student_with_lowest_score"]}

Passed: {summary["total_passed"]}
Unpassed: {summary["total_unpassed"]}
Pass rate: {summary["overall_pass_rate"]:.2f}%
Unacceptable scores: {summary["total_unacceptable_scores"]}
    """)
    else:
        print("No valid scores found.")
        print("Students without valid scores:",
              summary["students_without_scores"])


students = {}
while True:
    name = input("Enter student name: ")
    if name.lower() == "done":
        break
    str_scores = input("Enter student scores: ")

    scores = []

    for i in str_scores.split():
        try:
            scores.append(float(i))
        except ValueError:
            print(f"Invalid input ignored: {i}")
    students[name] = scores

summary = class_summary(students)
print_summary(summary)
