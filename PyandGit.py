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
    return minimum_score, maximum_score, average_score, passed, unpassed, unacceptable_scores


scores = [15, 18, 25, 12, -3, 20]
result = analyze_scores(scores)

if result is None:  # در صورت خالی بودن لیست نمره ها و برگرداندن نان توسط تابع ارور نمیدهد
    print("No Scores Available")  # و این را چاپ میکند
else:
    minimum, maximum, average, passed, unpassed, unacceptable = analyze_scores(
        scores)
    print(
        f"""
    Minimum score = {minimum}
    Maximum score = {maximum}
    Average of scores = {average} 
    passed : {passed} 
    unpassed : {unpassed}
    unacceptable scores :{unacceptable}""")
