assignments = [85, 90, 78]  # Assignment scores
quizzes = [80, 92]          # Quiz scores

# Weights for each category (total should be 1)
assignment_weight = 0.6
quiz_weight = 0.4

# Function to determine letter grade (A, B, C, F)
def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

# Calculate weighted total directly from individual scores
weighted_assignments = sum(score * (assignment_weight / len(assignments)) for score in assignments)
weighted_quizzes = sum(score * (quiz_weight / len(quizzes)) for score in quizzes)
overall_score = weighted_assignments + weighted_quizzes
