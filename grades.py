def grading_system(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B-" 
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Failed!"                    