def analyze_scores(scores):
    if not scores:  # در صورت خالی بودن لیست نمره ها اررور نمیدهد و نان را برمیگرداند
        return None

    minimum_score = 21
    maximum_score = -1
    total_score = 0
    passed = 0
    unpassed = 0
    unacceptable_scores = 0
    valid_scores_count = len(scores)

    for i in scores:
        if 0 <= i <= 20:
            if i >= 10:
                passed += 1
            else:
                unpassed += 1

            total_score += i
            if i > maximum_score:
                maximum_score = i
            elif i < minimum_score:
                minimum_score = i
        else:
            unacceptable_scores += 1
            valid_scores_count -= 1

    if valid_scores_count == 0:
        return None
    average_score = total_score/valid_scores_count
    pass_rate = passed / valid_scores_count * 100
    return {"minimum_score": minimum_score, "maximum_score": maximum_score,
            "average_score": average_score, "passed": passed, "unpassed": unpassed,
            "pass_rate": pass_rate, "unacceptable_scores": unacceptable_scores}


def class_summary(students):
    best_student = None
    worst_student = None
    student_with_highest_score = None
    student_with_lowest_score = None
    best_average = -1
    worst_average = 21
    maximum = -1
    minimum = 21
    total_passed = 0
    total_unpassed = 0
    total_unacceptable_scores = 0
    for name, scores in students.items():
        result = analyze_scores(scores)

        if result is None:
            print("No Scores Available")
        else:
            if best_average < result["average_score"]:
                best_average = result["average_score"]
                best_student = name
            if worst_average > result["average_score"]:
                worst_average = result["average_score"]
                worst_student = name
            if maximum < result["maximum_score"]:
                maximum = result["maximum_score"]
                student_with_highest_score = name
            if minimum > result["minimum_score"]:
                minimum = result["minimum_score"]
                student_with_lowest_score = name
            total_passed += result["passed"]
            total_unpassed += result["unpassed"]
            total_unacceptable_scores += result["unacceptable_scores"]
            print(
                f"""
            name = {name}
            Minimum score = {result["minimum_score"]}
            Maximum score = {result["maximum_score"]}
            Average of scores = {result["average_score"]:.2f}
            passed : {result["passed"]}
            unpassed : {result["unpassed"]}
            pass rate = {result["pass_rate"]:.2f}%
            unacceptable scores : {result["unacceptable_scores"]}"""
            )

    total_valid_scores = total_passed + total_unpassed

    if total_valid_scores == 0:
        return None
    overall_pass_rate = total_passed / total_valid_scores * 100
    return {"best_student": best_student, "best_average": best_average,
            "worst_student": worst_student, "worst_average": worst_average,
            "student_with_highest_score": student_with_highest_score, "highest_score": maximum,
            "student_with_lowest_score": student_with_lowest_score, "lowest_score": minimum,
            "total_passed": total_passed, "total_unpassed": total_unpassed,
            "total_unacceptable_scores": total_unacceptable_scores,
            "total_valid_scores": total_valid_scores,
            "overall_pass_rate": overall_pass_rate
            }


students = {
    "Ali": [15, 18, 12, 20, 17],
    "Reza": [9, 14, 25, 16, 8],
    "Sara": [19, 20, 18, 22, 17]
}


summary = class_summary(students)

print(f"""
            best student : {summary["best_student"]}
            best average : {summary["best_average"]:.2f}
            worst student : {summary["worst_student"]}
            worst average : {summary["worst_average"]:.2f}
            student with best score : {summary["student_with_highest_score"]}
            highest score : {summary["highest_score"]}
            student with lowest score : {summary["student_with_lowest_score"]}
            lowest score : {summary["lowest_score"]}
            total passed : {summary["total_passed"]}
            Total valid scores = {summary["total_valid_scores"]}
            Overall pass rate = {summary["overall_pass_rate"]:.2f}%
            total unpassed : {summary["total_unpassed"]}
            total_unacceptable_scores : {summary["total_unacceptable_scores"]}
    """)
