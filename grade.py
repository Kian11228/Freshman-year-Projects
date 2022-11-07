# grade.py
grade = int(input("PLase enter your grade: "))
if grade > 100:
    print("Invalid input!")
elif grade >= 90:
    print("You have an A!")
elif grade <= 89:
    print("You have a B!")
elif grade <= 79:
    print("you have a C!")
elif grade <= 70:
    print("you are failing")
elif grade < 0:
    print("Invalid input!")
