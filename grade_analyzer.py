from calculator import add, subtract, multiply, divide
def analyze_course():
    #basic info
    subject = input("Enter the subject name: ")
    num_assignments = int(input(f"How many assignments in {subject}? "))
    num_quizzes = int(input(f"How many quizzes in {subject}? "))

    total_assignment_score = 0
    total_quiz_score = 0
    total_assignment_weight = 0
    total_quiz_weight = 0

    for i in range(1, num_assignments + 1):
        score = float(input(f"Enter score for Assignment {i}: "))
        weight = float(input(f"Enter weightage for Assignment {i} (as percentage): "))
        weighted_score = multiply(score, divide(weight, 100))
        total_assignment_score = add(total_assignment_score, weighted_score)
        total_assignment_weight = add(total_assignment_weight, weight)

    for i in range(1, num_quizzes + 1):
        score = float(input(f"Enter score for Quiz {i}: "))
        weight = float(input(f"Enter weightage for Quiz {i} (as percentage): "))
        weighted_score = multiply(score, divide(weight, 100))
        total_quiz_score = add(total_quiz_score, weighted_score)
        total_quiz_weight = add(total_quiz_weight, weight)

    #total so far
    marks_so_far = add(total_assignment_score, total_quiz_score)
    total_weight_so_far = add(total_assignment_weight, total_quiz_weight)

    #percentage so far
    if total_weight_so_far > 0:
        percentage_so_far = multiply(divide(marks_so_far, total_weight_so_far), 100)
    else:
        percentage_so_far = 0


    total_course_weight = 100
    remaining_weight = subtract(total_course_weight, total_weight_so_far)

    #setting pass mark to 50
    pass_mark = 50

    #required mark to pass
    required_total_marks = multiply(pass_mark, divide(total_course_weight, 100))
    marks_needed = subtract(required_total_marks, marks_so_far)

    if remaining_weight > 0:
        percentage_needed = multiply(divide(marks_needed, remaining_weight), 100)
        if percentage_needed > 100:
            print("\nUnfortunately, it is not possible to reach the pass mark anymore.")
        elif percentage_needed <= 0:
            print("\nCongratulations! You are already passing the course.")
        else:
            print(f"\nYou need to score at least {marks_needed:.2f} marks in the remaining assessments.")
            print(f"That is {percentage_needed:.2f}% of the remaining weight to pass.")
    else:
        if marks_so_far >= pass_mark:
            print("\nCongratulations! You have already passed the course.")
        else:
            print("\nUnfortunately, you did not reach the pass mark.")

    #print results
    print("\n--- Report ---")
    print(f"Subject: {subject}")
    print(f"Marks so far: {marks_so_far:.2f} out of {total_weight_so_far}")
    print(f"Percentage so far: {percentage_so_far:.2f}%")
    print(f"Remaining weight: {remaining_weight:.2f}")
