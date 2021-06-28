marks = int(input("Enter the mark: "))
if marks>=80 and marks<=100:
    print("Grade: A+")
elif marks>=75 and marks<=79:
    print("Grade: A")
elif marks>=70 and marks<=74:
    print("Grade: A-")
elif marks>=65 and marks<=69:
    print("Grade: B+")
elif marks>=60 and marks<=64:
    print("Grade: B")
elif marks>=55 and marks<=59:
    print("Grade: B-")
elif marks>=50 and marks<=54:
    print("Grade: C+")
elif marks>=45 and marks<=49:
    print("Grade: C")
elif marks>=40 and marks<=44:
    print("Grade: D")
else:
    print("Grade:F")