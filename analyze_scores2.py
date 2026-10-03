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


# print(analyze_scores([15, 8, 17, 22, 5]))
# print(analyze_scores([]))
# print(analyze_scores([25, 30, -5]))
result1 = analyze_scores([15, 8, 17, 22, 5])
result2 = analyze_scores([])
result3 = analyze_scores([25, 30, -5])

print(result1)
print(result2)
print(result3)
scores = [15, 22, 8, -3, 19, 25, 10]
print(sum(score > 20 or score < 0 for score in scores))
# +sum(score < 0 for score in scores)
