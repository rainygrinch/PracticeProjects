# calculates the average score from three tests and produces a grade based on result

def calculate_average(quiz_score, midterm_score, final_score):
    total = quiz_score + midterm_score + final_score
    average = total / 3
    return average

def assign_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "Fail"


# Main program
quiz = float(input("Enter quiz score: "))
midterm = float(input("Enter midterm score: "))
final = float(input("Enter final score: "))

average = calculate_average(quiz, midterm, final)
grade = assign_grade(average)

print(f"Average Score: {average}")
print(f"Grade: {grade}")
