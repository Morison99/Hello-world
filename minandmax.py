# scores = [15, 18, 17, 12, -6, 20, 25]
# try:
#     print(max(score for score in scores if 0 <= score < 10))
# except ValueError:
#     print("No Valid Number")

# valid_scores = [score for score in scores if 0 <= score <= 20]

# if valid_scores:
#     minimum_score = min(valid_scores)
#     maximum_score = max(valid_scores)
# else:
#     minimum_score = None
#     maximum_score = None

scores = [18, 7, 21, 14, -2, 16]
valid_scores = [score for score in scores if 0 <= score <= 20]
if valid_scores:
    average = sum(valid_scores)/len(valid_scores)
    maximum = max(valid_scores)
    minimum = min(valid_scores)
    passed = sum(score >= 10 for score in valid_scores)
    unpassed = sum(score < 10 for score in valid_scores)
    pass_rate = passed / len(valid_scores) * 100
    print(f"""average : {average} 
maximum score = {maximum}
minimum score = {minimum}
number of passed = {passed}
number of unpassed = {unpassed}
pass rate = {pass_rate:.2f}""")
