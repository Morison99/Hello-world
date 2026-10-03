def analyze_scores(scores):
    valid_scores = [score for score in scores if 0 <= score <= 20]

    if not valid_scores:
        return None

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
        "unacceptable_scores": unacceptable_scores
    }


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
    sort_by_average = {}
    for name, scores in students.items():
        result = analyze_scores(scores)
        if result is None:
            print("No Scores Available")
        else:
            sort_by_average[name] = result["average_score"]
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
            total_passed += result["total_passed"]
            total_unpassed += result["total_unpassed"]
            total_unacceptable_scores += result["unacceptable_scores"]

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
        ranking.append((rank, key, value))
        counter += 1
        pre_value = value

    # ==========================================================
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
            "overall_pass_rate": overall_pass_rate,
            "student_ranking": ranking
            }


students = {
    "Ali": [18, 18],
    "Reza": [16, 20],
    "Sara": [15, 15]
}

summary = class_summary(students)
# for counter, (name, average) in enumerate(summary["student_ranking"], start=1):
#     print(f"{counter} . {name} : {average}")
print(summary["student_ranking"])
