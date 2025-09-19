marks = int(input("ENTER YOUR MARKS (0-100): "))
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter a number between 0 and 100.")
    elif marks >= 80:
        print (f"YOUR GRADE IS: A+")
    elif marks >= 75:
        print (f"YOUR GRADE IS: B+")
    elif marks >= 60:
        print (f"YOUR GRADE IS: C+")
    elif marks >=50:
        print (f"YOUR GRADE IS: D+")
    else:
        print ("FAIL")

calculate_grade(marks)